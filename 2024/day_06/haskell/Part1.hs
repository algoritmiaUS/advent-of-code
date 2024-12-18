{-# LANGUAGE LambdaCase #-}
{-# LANGUAGE LinearTypes #-}
{-# LANGUAGE OverloadedRecordDot #-}
{-# LANGUAGE StrictData #-}

import Control.Monad hiding (guard)
import Data.Bifunctor
import Data.Foldable
import Data.List
import Data.Maybe
import Data.Set as S
  ( Set,
    empty,
    fromList,
    insert,
    member,
    notMember,
  )
import Text.Read

data Point = Point {x :: Int, y :: Int} deriving (Eq, Ord)

data EntityType = Guard | Obstacle deriving (Eq)

data Entity = Entity {eCoords :: Point, eType :: EntityType}

instance Read EntityType where
  readPrec = do
    c <- get
    case c of
      '#' -> pure Obstacle
      '^' -> pure Guard
      _ -> pfail

getEntities :: [String] -> [Entity]
getEntities = catMaybes . fold . zipWith (\y l -> zipWith (readAndBuild y) [0 ..] l) [0 ..]
  where
    readAndBuild y x k = Entity (Point x y) <$> readMaybe [k]

both :: (Bifunctor p) => (c -> d) -> p c c -> p d d
both f = bimap f f

separate es = case both (fmap eCoords) $ partition ((== Obstacle) . eType) es of
  (obstacles, [gc]) -> Just (S.fromList obstacles, gc)
  _ -> Nothing

parse :: String -> Maybe Grid
parse s = do
  let plane = lines s
      lengthY = length plane
  lengthX <- listToMaybe $ fmap length plane
  (obstacles, gc) <- separate . getEntities $ plane
  pure $
    Grid
      { obstacles,
        guardStart = Position {coords = gc, direction = F},
        maxC = Point {x = lengthX - 1, y = lengthY - 1}
      }

data Orientation = F | R | B | L deriving (Eq, Ord, Enum, Bounded, Show)

data Position = Position
  { coords :: Point,
    direction :: Orientation
  }
  deriving (Eq, Ord)

data Grid = Grid
  { obstacles :: Set Point,
    guardStart :: Position,
    maxC :: Point
  }

succPosition :: Position -> Position
succPosition pos@Position {coords, direction = d} = case d of
  F -> pos {coords = coords {y = coords.y - 1}}
  R -> pos {coords = coords {x = coords.x + 1}}
  B -> pos {coords = coords {y = coords.y + 1}}
  L -> pos {coords = coords {x = coords.x - 1}}

steerLeft :: Orientation %1 -> Orientation
steerLeft = \case
  F -> R
  R -> B
  B -> L
  L -> F

changeDir :: Position %m -> Position
changeDir Position {coords, direction} =
  Position
    { coords,
      direction = steerLeft direction
    }

data WalkState = WalkState {past :: Set Position, guard :: Position}

isWithinFrame :: Point -> Point -> Bool
p `isWithinFrame` maxC = 0 <= p.x && p.x <= maxC.x && 0 <= p.y && p.y <= maxC.y

iterateMaybe :: (a -> Maybe a) -> a -> [a]
iterateMaybe f !x = x : maybe [] (iterateMaybe f) (f x)

succPositionWhen :: (Point -> Bool) -> Position -> Maybe Position
succPositionWhen isValid =
  find (isValid . coords) . fmap succPosition . take 4 . iterate changeDir

moveWhile :: (Point -> Bool) -> (Point -> Bool) -> WalkState -> Maybe WalkState
moveWhile isWithinLimits isValid ws = do
  guard' <-
    mfilter (isWithinLimits . coords) $
      succPositionWhen isValid ws.guard
  pure WalkState {past = ws.guard `S.insert` ws.past, guard = guard'}

keepMovingWhile :: (Point -> Bool) -> (Point -> Bool) -> WalkState -> [WalkState]
keepMovingWhile isWithinLimits isValid =
  iterateMaybe (moveWhile isWithinLimits isValid)

hitsLoop :: WalkState -> Bool
hitsLoop WalkState {past, guard} = guard `S.member` past

mainPath :: Grid -> [WalkState]
mainPath field =
  keepMovingWhile (`isWithinFrame` field.maxC) (`S.notMember` field.obstacles) $
    WalkState {past = S.empty, guard = field.guardStart}

solve = length . S.fromList . fmap (coords . guard) . takeWhile (not . hitsLoop) . mainPath

run = fmap solve . parse

main = print . run =<< readFile "input.txt"