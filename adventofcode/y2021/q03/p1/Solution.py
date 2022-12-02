from io import TextIOWrapper
import math


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    res = 0
    cols = list(zip(*lines))
    n = len(lines)
    sum_of_each_col = [sum(list(map(int, col))) for col in cols]
    gamma_rate_bin = ''.join(
        ['1' if total > n // 2 else '0' for total in sum_of_each_col])
    epsilon_rate_bin = ''.join(
        ['0' if char == '1' else '1' for char in gamma_rate_bin])
    gamma_rate, epsilon_rate = int(gamma_rate_bin, 2), int(epsilon_rate_bin, 2)
    res = gamma_rate * epsilon_rate

    # Finish your codes here
    return res
