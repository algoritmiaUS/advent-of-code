import Data.Maybe
import Text.Parsec

instruction = between (string "mul(") (char ')') $ do
    x <- many1 digit
    char ','
    y <- many1 digit
    pure (read x :: Int, read y :: Int)

search p = many loop
    where loop = try p <|> try (anyChar >> loop)

getInstructions = parse (search instruction) "instructions.txt"

sumMultiplications = sum . fmap (uncurry (*))

main = print . fmap sumMultiplications . getInstructions =<< readFile "input.txt"
