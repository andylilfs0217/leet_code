from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = 0
    nums = [int(num) for num in lines]
    prev = nums[0]
    for i in range(1, len(nums)):
        curr = nums[i]
        if curr > prev:
            res += 1
        prev = curr

    # Finish your codes here
    return res
