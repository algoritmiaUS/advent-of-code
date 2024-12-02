"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""

safe_reports = 0

with open("./2024/day_02/input/input.txt") as f:
    for line in f:
        last, *nums = list(map(int, line.split()))
        increasing = None

        safe = True
        for num in nums:
            if (
                not (increasing is True and 0 < num - last <= 3)
                and not (increasing is False and 0 < last - num <= 3)
                and not (increasing is None and 0 < abs(last - num) <= 3)
            ):
                safe = False
                break

            increasing = last < num
            last = num

        safe_reports += safe

print(safe_reports)

with open("./2024/day_02/input/output_1.txt", "w") as f:
    f.write(f"{safe_reports}\n")
