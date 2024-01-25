function processing(lines)
   mat = fill(Char(0), length(lines), length(lines[1]))
   for i in range(1,length(lines))
        for j in range(1,length(lines[1]))
            mat[i,j] = lines[i][j]
        end
   end
   return mat

end

function get_neighbours(grid, row, column)
    neighbours = []
    directions = [
        (-1, 0), 
        (1, 0),
        (0, -1), 
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    ]

    for (dx,dy) in directions

        new_row, new_column = row + dx, column + dy
        if (1 <= new_row <= size(grid)[1]) && (1 <= new_column <= size(grid)[2])

            if (isdigit(grid[new_row,new_column]))
                push!(neighbours, (new_row, new_column))
            end
        end


    end

    return neighbours

end

function get_num_neighbours(grid, neighbours)
    nums = []

    for (i, j) in neighbours
        num = grid[i, j]

        # Left
        pos_l = j - 1
        while pos_l > 0 && isdigit(grid[i, pos_l])
            num = grid[i, pos_l] * num
            pos_l -= 1
        end

        # Right
        pos_r = j + 1
        while pos_r <= size(grid, 2) && isdigit(grid[i, pos_r])
            num = num * grid[i, pos_r]
            pos_r += 1
        end

        push!(nums, parse(Int, num))
    end
    return Set(nums)
end


function part1(data)
    acc = 0
    rows, columns = size(data)
    for i in 1:rows
        for j in 1:columns
            # Find a symbol
            if (data[i,j] != '.') && !isdigit(data[i,j])
                # Select valid neighbours
                symbol = data[i,j]
                # println("Posición symbol $i $j $symbol")
                neighbours = get_neighbours(data, i, j)
                num_neighbours = sum(get_num_neighbours(data, neighbours))
                # println(neighbours)
                # println([data[i,j] for (i,j) in neighbours])
                # println(num_neighbours)
                # println("=========================")
                acc += num_neighbours

                  


            end
            
        end
        
    end

    return acc

end

function part2(data)
    acc = 0
    rows, columns = size(data)
    for i in 1:rows
        for j in 1:columns
            # Find a symbol
            if (data[i, j] != '.') && !isdigit(data[i, j])
                # Select valid symbol (*)
                symbol = data[i, j]
                if symbol == '*'
                    neighbours = get_neighbours(data, i, j)
                    num_neighbours = get_num_neighbours(data, neighbours)
                    if length(num_neighbours) == 2
                        acc += prod(collect(num_neighbours)) 
                    end
                end
            end
        end
    end

    return acc
end


function day3()

    # Read file
    f = open("day3/input.txt", "r")
    lines = readlines(f)
    close(f)

    # processing data
    data = processing(lines)
    
    # part1
    println(part1(data))

    # part2
    println(part2(data))

end



day3()