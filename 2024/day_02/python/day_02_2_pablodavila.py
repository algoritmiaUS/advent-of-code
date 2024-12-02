"""Solution by Pablo Dávila Herrero (https://pablodavila.eu)"""


def is_safe(report):
    last, *nums = report
    increasing = None
    for num in nums:
        if (
            not (increasing is True and 0 < num - last <= 3)
            and not (increasing is False and 0 < last - num <= 3)
            and not (increasing is None and 0 < abs(last - num) <= 3)
        ):
            return False

        increasing = last < num
        last = num

    return True


safe_reports = 0

with open("./2024/day_02/input/input.txt") as f:
    for line in f:
        report = list(map(int, line.split()))

        safe_reports += (
            is_safe(report)
            or any(
                is_safe(report[:i]+report[i+1:])
                for i in range(len(report))
            )
        )

print(safe_reports)

with open("./2024/day_02/input/output_2.txt", "w") as f:
    f.write(f"{safe_reports}\n")
