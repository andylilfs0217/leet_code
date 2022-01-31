from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[1] <= arr[0]:
            return False
        is_climbing_up = True
        for i in range(1, len(arr)):
            if is_climbing_up and arr[i] < arr[i - 1]:
                is_climbing_up = False
            if (not is_climbing_up and arr[i] > arr[i - 1]) or arr[i] == arr[i - 1]:
                return False
        return not is_climbing_up
