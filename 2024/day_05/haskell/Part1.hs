import Control.Applicative
import Data.Bifunctor
import Data.Function
import Data.IntMap.Strict as M
import Data.IntSet as S
import Data.List as L
import Data.Maybe
import Data.Tuple
import Text.Read

isPageWellPlaced succMap preds p = fromMaybe True $ do
  succs <- succMap !? p
  pure . all (`S.notMember` succs) $ preds

isCorrectOrd :: IntMap IntSet -> [Key] -> Bool
isCorrectOrd m = all (maybe True (uncurry (isPageWellPlaced m) . swap) . uncons . reverse) . inits

getMapOfSuccs = M.fromListWith (<>) . fmap (second S.singleton)

middle xs = last . zipWith const xs . L.filter (even . fst) . zip [0..] $ xs

solve orderings = sum . fmap middle . L.filter (isCorrectOrd (getMapOfSuccs orderings))

changeToSpace c x
  | x == c = ' '
  | otherwise = x

parseEachOrd = uncurry (liftA2 (,) `on` readMaybe) . second tail . break (== '|')

parseOrds = traverse parseEachOrd

parseEachUpd = traverse readMaybe . words . fmap (changeToSpace ',')

parseUpds = traverse parseEachUpd

parse :: String -> Maybe ([(Int, Int)], [[Int]])
parse = uncurry (liftA2 (,)) . bimap parseOrds (parseUpds . tail) . break L.null . lines

run = fmap (uncurry solve) . parse

main = print . run =<< readFile "input.txt"