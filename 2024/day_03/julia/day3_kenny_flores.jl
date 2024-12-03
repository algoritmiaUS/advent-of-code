# Solution by Kenny Jesús Flores Huamán (https://kennyfh.github.io/)

f = open("../input/input.txt", "r")
lines = readlines(f)
memory = join(lines, "")

function part1(memory)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    coincidences = collect(eachmatch(pattern, memory))
    acc = 0
    for c in coincidences
        acc += (parse(Int, c.captures[1])*parse(Int, c.captures[2]))
    end
    return acc
end


function part2(memory)
    pattern = r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)"
    enabled = true
    sum = 0
    
    for m in eachmatch(pattern, memory)
        if m.match == "do()"
            enabled = true
        elseif m.match == "don't()"
            enabled = false
        elseif enabled
            sum += parse(Int, m.captures[1]) * parse(Int, m.captures[2])
        end
    end
    
    return sum
end

println("El resultado de part1 es: $(part1(memory))") # 167090022
println("El resultado de part2 es: $(part2(memory))") # 89823704


close(f)




