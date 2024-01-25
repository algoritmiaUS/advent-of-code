function get_fst_lst(line, part2)
    if part2
        line = replace(line, "twone" =>"twoone",
                             "oneight" => "oneeight",
                             "eightwo" => "eighttwo",
                             "fiveight" => "fiveeight",
                             "threeight" => "threeeight")
        line = replace(line, "one" => 1,
            "two" => 2,
            "three" => 3,
            "four" => 4,
            "five" => 5,
            "six" => 6,
            "seven" => 7,
            "eight" => 8,
            "nine" => 9
        )


    end
    nums = [x for x in line if isdigit(x)]
    if length(nums) < 2
        return nums[1] * nums[1]
    end
    return nums[1] * nums[end]
end


function day1(part2=false)
    f = open("day1/input.txt", "r")
    lines = readlines(f)
    close(f)
    return [parse(Int, get_fst_lst(line, true)) for line in lines] |> sum

end


day1(true)
