# Solution by Kenny Jesús Flores Huamán (https://kennyfh.github.io/)


f = open("../input/input.txt", "r")
lines = readlines(f)

left = Int[]
right = Int[]

for line in lines
    x,y = split(line)
    push!(left,parse(Int, x))
    push!(right,parse(Int, y))

end 


function part1(arr1, arr2)
    sort!(left)
    sort!(right)
    distance = 0
    for (x,y) in zip(arr1,arr2)
        distance += abs(x-y)
    end
    return distance
end

function part2(arr1,arr2)
    counter = Dict()
    for item in arr2
        counter[item] = get(counter, item, 0) + 1
    end

    similarity  = 0

    for item in Set(arr1)

        similarity += item * get(counter, item, 0)
        
    end

    return similarity 

end

println("El resultado de part1 es: $(part1(left, right))")
println("El resultado de part2 es: $(part2(left,right))")


close(f)




