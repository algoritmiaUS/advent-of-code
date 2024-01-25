# function processing(lines)
#     dicc = Dict{Int, Vector{Tuple{Int, Int, Int}}}()

#     # Loop lines
#     for (idx, line) in enumerate(lines)
#         set_acc = Vector{Tuple{Int, Int, Int}}()

#         _, games = split(line, ":")

#         for game in split(games, ";")
#             aux = Dict("red" => 0, "green" => 0, "blue" => 0)

#             for c in split(strip(game), ", ")
#                 num, color = split(c, " ")
#                 aux[color] = parse(Int, num)
#             end

#             push!(set_acc, (aux["red"], aux["green"], aux["blue"]))
#         end

#         dicc[idx] = set_acc
#     end
    
#     return dicc
# end


function processing(lines)
    dicc = Dict{Int, Vector{Tuple{Int, Int, Int}}}()

    # Recorre las líneas
    for (idx, line) in enumerate(lines)
        set_acc = Vector{Tuple{Int, Int, Int}}()

        _, games = split(line, ":")

        for game in split(games, ";")
            aux = Dict(1 => 0, 2 => 0, 3 => 0)

            for c in split(strip(game), ", ")
                num, color = split(c, " ")
                aux[findfirst(x -> x == color, ["red", "green", "blue"])] = parse(Int, num)
            end

            push!(set_acc, (aux[1], aux[2], aux[3]))
        end

        dicc[idx] = set_acc
    end

    return dicc
end


function part1(games)
    acc = 0

    for (k, v) in games
        if all(t -> t[1] <= 12 && t[2] <= 13 && t[3] <= 14, v)
            println(k)
            acc += k
        end
    end

    return acc
end

function part2(games)
    return sum(prod(maximum(x -> x[i], v) for i in 1:3) for v in values(games))

end

function day2()
    # Read files
    f = open("day2/input.txt", "r")
    lines = readlines(f)
    close(f)

    data = processing(lines) # {1: [(12, 12, 12), (1, 3, 4), ...], 2: ....}
    # print(data)

    # part1
    println(part1(data)) # 2416

    # part2
    println(part2(data)) # 63307   
end

day2()

