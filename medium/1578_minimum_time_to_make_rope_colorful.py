from typing import List


class Solution:

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # return self.minCost1(colors, neededTime)
        return self.minCost2(colors, neededTime)

    def minCost1(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        needed_time_dp = [0]
        temp = 0
        ans = 0
        for time in neededTime:
            temp += time
            needed_time_dp.append(temp)
        l, r = 0, 1
        curr_max_time = needed_time_dp[0]
        while r < n:
            l_color, r_color = colors[l], colors[r]
            time = neededTime[r]
            if l_color == r_color:
                # Same group
                curr_max_time = max(curr_max_time, neededTime[r])
            elif r - l > 1:
                l_total_time = needed_time_dp[l]
                r_total_time = needed_time_dp[r]
                total_time = r_total_time - l_total_time
                used_time = total_time - curr_max_time
                ans += used_time
                curr_max_time = neededTime[r]
                l = r
            else:
                curr_max_time = neededTime[r]
                l = r
            r += 1
        if r - l > 1:
            l_total_time = needed_time_dp[l]
            r_total_time = needed_time_dp[r]
            total_time = r_total_time - l_total_time
            used_time = total_time - curr_max_time
            ans += used_time
        return ans

    def minCost2(self, colors: str, neededTime: List[int]) -> int:
        # Initalize two pointers i, j.
        total_time = 0
        i, j = 0, 0

        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0

            # Find all the balloons having the same color as the
            # balloon indexed at i, record the total removal time
            # and the maximum removal time.
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1

            # Once we reach the end of the current group, add the cost of
            # this group to total_time, and reset two pointers.
            total_time += curr_total - curr_max
            i = j

        return total_time


print(Solution().minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5]))
print(Solution().minCost(colors="abc", neededTime=[1, 2, 3]))
print(Solution().minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1]))
