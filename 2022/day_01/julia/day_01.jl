# Solution by Kenny Flores 

function part1(data)
    acc = 0
    max_number = 0

    for num in data
        if isa(tryparse(Float64,num), Number) 
            acc+= parse(Int, num)
        else
            if acc > max_number
                max_number=acc
            end
            acc=0
        end

    end

    return max_number
end

function part2(data)
    acc = []
    aux = []
    for num in data
        if isa(tryparse(Float64,num), Number)
            push!(aux, parse(Int,num))
        else
            calories = sum(aux)
            push!(acc, calories)
            aux= []
        end
    end 

    return acc |> x-> sort(x,rev=true) |> x -> x[1:3] |> sum

end

function day1()
    # Read file
    f = open("./2022/day_01/input/input.txt", "r")
    lines = readlines(f)
    close(f)

    # Part 1 
    println(part1(lines))
    # Part 2
    print(part2(lines))
    

end

day1()