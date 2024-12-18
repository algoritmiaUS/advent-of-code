import Data.Maybe
import Text.Parsec

data Instruction = Mul Int Int
                 | Disable
                 | Enable

multiply = between (string "mul(") (char ')') $ do
    x <- many1 digit
    char ','
    y <- many1 digit
    pure $ Mul (read x) (read y)

disable = string "don't()" >> pure Disable

enable = string "do()" >> pure Enable

instruction = try multiply <|> try disable <|> enable

search p = many loop
    where loop = try p <|> try (anyChar >> loop)

getInstructions = parse (search instruction) "instructions.txt"

skipInstructions _    []     = []
skipInstructions skip (x:xs) = case x of
    (Mul a b) -> if skip then skipInstructions skip xs else (a, b) : skipInstructions skip xs
    Disable   -> skipInstructions True  xs
    Enable    -> skipInstructions False xs

sumMultiplications = sum . fmap (uncurry (*))

main = print . fmap (sumMultiplications . skipInstructions False) . getInstructions =<< readFile "input.txt"
