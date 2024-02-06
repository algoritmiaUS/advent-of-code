
function part1(data)
    acc = 0

    for pairs in data
        pairs = split(pairs, ",") # 98-99 3-97
        a,b = [parse(Int,x) for x in split(pairs[1],"-")] # 98-99
        c,d = [parse(Int,x) for x in split(pairs[2],"-")] # 3-97

        if (c >=a && d<=b) || (a >= c && b<=d)
            acc+=1  
            
        end

    end

    return acc
end

function part2(data)
    acc=0
    for pairs in data
        pairs = split(pairs, ",") # 98-99 3-97
        a,b = [parse(Int,x) for x in split(pairs[1],"-")] # 98-99
        c,d = [parse(Int,x) for x in split(pairs[2],"-")] # 3-97

        if min(b,d) >= max(a,c)
           acc+=1 
        end
    end
    return acc
end


function day4()
    f = open("./2022/day_04/input/input_jl.txt")
    lines = readlines(f)
    close(f)

    # Part1
    println(part1(lines))

    println(part2(lines))


end


day4()