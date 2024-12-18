{-# LANGUAGE LambdaCase #-}

import Data.Function
import Data.Ix
import Data.List
import Data.Maybe
import Text.Read

mapAdjacent f (a:bs@(b:_)) = f a b : mapAdjacent f bs
mapAdjacent _ _            = []

unsnoc :: [a] -> Maybe ([a], a)
unsnoc = foldr (\x -> Just . maybe ([], x) (\(~(a, b)) -> (x : a, b))) Nothing

isValidDelta = inRange (1, 3) . abs

deltaMonotonicGroups = groupBy ((==) `on` signum) . mapAdjacent (-)

extractMonoGroup = \case
    []          -> Just []
    [a]         -> Just a
    _           -> Nothing

checkLine = maybe False (all isValidDelta) . extractMonoGroup . deltaMonotonicGroups

solve = length . filter checkLine

parse = mapMaybe (traverse readMaybe . words) . lines

run = solve . parse

main = print . run =<< readFile "input1.txt"
