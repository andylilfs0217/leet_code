import math


class Solution:
    def numWays(self, s: str) -> int:
        num_of_ones = s.count('1')
        num_of_zeros = s.count('0')
        if num_of_ones % 3 != 0:
            return 0
        if num_of_ones == 0:
            return math.comb(num_of_zeros-1, 2) % (10**9 + 7)
        splits = [-1] * 4
        split_idx = 0
        curr_num_of_ones = 0
        for i, char in enumerate(s):
            if char == '1':
                curr_num_of_ones += 1
                if curr_num_of_ones == num_of_ones // 3:
                    splits[split_idx] = i
                    split_idx += 1
                if curr_num_of_ones == num_of_ones // 3 + 1:
                    splits[split_idx] = i
                    split_idx += 1
                if curr_num_of_ones == (num_of_ones // 3) * 2:
                    splits[split_idx] = i
                    split_idx += 1
                if curr_num_of_ones == (num_of_ones // 3) * 2 + 1:
                    splits[split_idx] = i
                    split_idx += 1
        first_split_n = splits[1] - splits[0]
        second_split_n = splits[3] - splits[2]
        ans = (first_split_n * second_split_n) % (10**9 + 7)
        return ans
