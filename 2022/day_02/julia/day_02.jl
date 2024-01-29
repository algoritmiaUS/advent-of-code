# Solution by Kenny Flores 

function part1(data)
    # A: Rock, B: Paper, C: Scissors
    # X: Rock, Y: Paper, Z: Scissors
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won

    dicc = Dict("A X" => 1+3,  # Rock vs. Rock (Draw)
                "A Y" => 2+6,  # Rock vs. Paper (Paper wins)
                "A Z" => 3+0,  # Rock vs. Scissors (Rock wins)
                "B X" => 1+0,  # Paper vs. Rock (Paper wins)
                "B Y" => 2+3,  # Paper vs. Paper (Draw)
                "B Z" => 3+6,  # Paper vs. Scissors (Scissors wins)
                "C X" => 1+6,  # Scissors vs. Rock (Rock wins)
                "C Y" => 2+0,  # Scissors vs. Paper (Scissors wins)
                "C Z" => 3+3,  # Scissors vs. Scissors (Draw)
                )

    return map(x -> dicc[x], data) |> sum 
end

function part2(data)

    # A: Rock, B: Paper, C: Scissors
    # X: lose, Y: draw, Z: win
    # 1 for Rock, 2 for Paper, and 3 for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won

    dicc = Dict("A X" => 3+0, # You are Scissors
                "B X" => 1+0, # You are Rock
                "C X" => 2+0, # You are paper

                "A Y" => 1+3,  
                "B Y" => 2+3,
                "C Y" => 3+3,

                "A Z" => 2+6,    
                "B Z" => 3+6,  
                "C Z" => 1+6, 
                 
                )
    return map(x -> dicc[x], data) |> sum 

end


function day2()
    f = open("./2022/day_02/input/input.txt", "r")
    lines =  readlines(f)
    close(f)

    # Part 1
    println(part1(lines))

    # Part2
    println(part2(lines))
end 

day2()