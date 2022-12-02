from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    # res = Solution1(f)
    res = Solution2(f)
    return res


# Part 1
def Solution1(f: TextIOWrapper):
    lines = f.readlines()
    res = 0

    # Write your codes here
    curr_cal = 0

    for line in lines:
        if line == '\n':
            res = max(res, curr_cal)
            curr_cal = 0
        else:
            cal = int(line)
            curr_cal += cal

    # Finish your codes here
    return res


# Part 2
def Solution2(f: TextIOWrapper):
    lines = f.readlines()
    res = 0

    # Write your codes here
    top_three = [0, 0, 0]
    curr_cal = 0

    for line in lines:
        if line == '\n':
            if curr_cal > top_three[-1]:
                top_three[-1] = curr_cal
                top_three.sort(reverse=True)
            curr_cal = 0
        else:
            cal = int(line)
            curr_cal += cal
    if curr_cal > top_three[-1]:
        top_three[-1] = curr_cal
        top_three.sort(reverse=True)

    res = sum(top_three)

    # Finish your codes here
    return res