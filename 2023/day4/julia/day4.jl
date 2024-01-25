# Preprocessing
function preprocessing(lines)
    winning_list = []
    ticket_list = []
    for line in lines
        _, ls_nums = split(line, ':') 
        winning_nums, ticket_nums = split(ls_nums, '|') # winning_nums = " 1 2 3 4 5 6 7", ticket_nums = " 8 9 10 11 12 13 14"
        winning_nums = split(winning_nums) # winning_nums = ["1", "2", "3", "4", "5", "6", "7"]
        ticket_nums = split(ticket_nums) # ticket_nums = ["8", "9", "10", "11", "12", "13", "14"]
        push!(winning_list, winning_nums)
        push!(ticket_list, ticket_nums)
    end
    
    return (winning_list, ticket_list)
end

# Part 1 
function calculate_points(winning, ticket)
    n = 0
    # winning, ticket = card
    for t in ticket
        if t in winning
            n += 1
        end
    end

    score = n > 0 ? 2^(n-1) : 0
    return score
end


function part1(winning, ticket)
    return map(calculate_points, winning, ticket) |> sum
end


function part2(winning, tickets)
    dicc = Dict()
    for i in 1:length(winning)
        if !(i in keys(dicc))
            dicc[i] = 1
        end

        j = length(intersect(Set(winning[i]), Set(tickets[i])))
        
        for n in i+1:i+j
            dicc[n] = get(dicc, n, 1) + dicc[i]
        end
        
    end


    return sum(values(dicc))


end



function day4()
    f = open("day4/input.txt", "r")
    lines = readlines(f)
    close(f)

    winning, tickets = preprocessing(lines)

    # Part 1
    println(part1(winning, tickets))

    # Part 2 
    println(part2(winning, tickets))


end

day4()