import Control.Applicative
import Control.Monad
import Data.Bifunctor
import Data.Foldable as F
import Data.Function
import Data.IntMap.Strict as M hiding (mapMaybe)
import Data.IntSet as S
import Data.List as L
import Data.Maybe
import Data.Sequence as Seq
import Data.Tuple
import Text.Read

isPageWellPlaced succMap preds p = fromMaybe True $ do
  succs <- succMap M.!? p
  pure . all (`S.notMember` succs) $ preds

getMapOfSuccs = M.fromListWith (<>) . fmap (second S.singleton)

middle xs = Seq.index xs $ Seq.length xs `quot` 2

insertInOrder succMap seq x = fromMaybe (seq :|> x) $ do
  succs <- succMap M.!? x
  p <- fmap fst . find ((`S.member` succs) . snd) . L.zip [0 ..] . F.toList $ seq
  pure $ insertAt p x seq

unsnoc = L.foldr (\x -> Just . maybe ([], x) (\(~(a, b)) -> (x : a, b))) Nothing

correctedOrdOrSkip succMap update = do
  let (toReinsert, cleanSeq) = bimap (fmap snd) (Seq.fromList . fmap snd) . L.partition (not . uncurry (isPageWellPlaced succMap)) . mapMaybe unsnoc . L.inits $ update
  guard . not . L.null $ toReinsert
  pure . L.foldl' (insertInOrder succMap) cleanSeq $ toReinsert

solve orderings = sum . fmap middle . mapMaybe (correctedOrdOrSkip succMap)
  where
    succMap = getMapOfSuccs orderings

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