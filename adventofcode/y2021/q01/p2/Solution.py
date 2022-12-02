from io import TextIOWrapper


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    SLIDING_WINDOW = 3
    res = 0
    nums = [int(num) for num in lines]
    prev_sum = sum(nums[:SLIDING_WINDOW])
    for l in range(len(nums) - SLIDING_WINDOW):
        r = l + SLIDING_WINDOW
        num_l, num_r = nums[l], nums[r]
        curr_sum = prev_sum - num_l + num_r
        if curr_sum > prev_sum:
            res += 1
        prev_sum = curr_sum

    # Finish your codes here
    return res
