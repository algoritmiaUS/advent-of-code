import Control.Monad
import Data.Bifunctor
import Data.IntMap.Strict as M (fromListWith, toAscList)
import Data.Maybe
import Text.Read

both :: (Bifunctor p) => (c -> d) -> p c c -> p d d
both f = bimap f f

absDiff :: (Num a) => a -> a -> a
absDiff x y = abs (x - y)

counter = M.fromListWith (+) . fmap (,1)

solve = sum . fmap (uncurry absDiff) . uncurry zip . both (uncurry (flip replicate) <=< M.toAscList . counter) . unzip

parse = mapMaybe (fmap (\(a : b : _) -> (a, b)) . traverse readMaybe . words) . lines

run = solve . parse

main = print . run =<< readFile "input.txt"
