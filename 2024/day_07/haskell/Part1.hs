import Data.Bifunctor
import Data.IntSet as S
import Data.List as L
import Data.List.NonEmpty
import Text.Read

evalResults ops (n :| ns@(n' : ns')) = foldMap (\op -> evalResults ops (op n n' :| ns')) ops
evalResults ops (n :| []) = [n]

possibleResults = S.fromList . evalResults [(+), (*)]

solve :: [(Int, NonEmpty Int)] -> Int
solve = sum . fmap fst . L.filter (uncurry S.member . second possibleResults)

unsnoc = L.foldr (\x -> Just . maybe ([], x) (\(~(a, b)) -> (x : a, b))) Nothing

parseLine l = case words l of
  (r' : (n : ns')) -> case unsnoc r' of
    Just (r, ':') -> (,) <$> readMaybe r <*> traverse readMaybe (n :| ns')
    Nothing -> Nothing
  _ -> Nothing

parse = traverse parseLine . lines

run = fmap solve . parse

main = print . run =<< readFile "input.txt"
