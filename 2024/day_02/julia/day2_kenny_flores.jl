# Solution by Kenny Jesús Flores Huamán (https://kennyfh.github.io/)


f = open("../input/input.txt", "r")
lines = readlines(f)

reports = [[parse(Int, x) for x in split(line)]  for line in lines]

function is_safe_report(report)::Bool
    # The levels are either all increasing or all decreasing.
    if !(issorted(report) || issorted(report, by = x -> -x))
        return false
    end

    diffs = abs.(diff(report))
    return all(1 .<= diffs .<= 3 )

end

function part1(reports)
    count = 0

    for report in reports
        # Monotonía, todo debe aumentar o disminuir
        if is_safe_report(report)
            count +=1
        end

    end

    return count
end

function problem_dampener(report)
    
    for i in 1:length(report)
        remaining_elements = [report[1:i-1]; report[i+1:end]]
        if is_safe_report(remaining_elements)
            return 1
        end

    end
    
    return 0
end

function part2(reports)
    count = 0

    for report in reports

        if is_safe_report(report)
            count+=1
        else
            count+=problem_dampener(report)
        end
    end
    return count
end


println("El resultado de part1 es: $(part1(reports))") # 359
println("El resultado de part2 es: $(part2(reports))") # 418


close(f)




