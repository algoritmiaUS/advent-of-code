import Control.Monad
import Data.Bifunctor
import Data.IntMap.Strict as M (fromListWith, lookup, toAscList)
import Data.Maybe
import Data.Tuple
import Text.Read
import Prelude hiding (lookup)

lookupAndMul x m = x * fromMaybe 0 (x `lookup` m)

counter = M.fromListWith (+) . fmap (,1)

solve = sum . uncurry (fmap . flip lookupAndMul) . first counter . swap . unzip

parse = mapMaybe (fmap (\(a : b : _) -> (a, b)) . traverse readMaybe . words) . lines

run = solve . parse

main = print . run =<< readFile "input.txt"