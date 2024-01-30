

function part1(rucksacks)
    acc = 0
    dicc = Dict(letter => i for (i, letter) in enumerate(['a':'z'; 'A':'Z']))

    for r in rucksacks
        mid = div(length(r), 2)
        l = Set(r[1:mid])
        for e in r[mid+1:end] # Julia have 1-indexing
            if e in l
                acc += dicc[e]
                break
            end
        end
    end

    return acc
end

function part2(rucksacks)
    acc = 0
    dicc = Dict(letter => i for (i, letter) in enumerate(['a':'z'; 'A':'Z']))
    for i in 1:3:length(rucksacks)
        acc+= dicc[first(intersect(Set(rucksacks[i]), Set(rucksacks[i+1]), Set(rucksacks[i+2])))]
    end
    return acc
end

function day3()
    f = open("./2022/day_03/input/input.txt")
    lines = readlines(f)
    close(f)

    # Part1
    println(part1(lines))

    println(part2(lines))


end


day3()
