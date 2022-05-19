from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return self.nextGreaterElement1(nums1, nums2)
        return self.nextGreaterElement2(nums1, nums2)

    # Time: O(n*m)
    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        n, m = len(nums1), len(nums2)
        for num1 in nums1:
            i = nums2.index(num1)
            bigger_num = -1
            for j in range(i+1, m):
                if nums2[j] > num1:
                    bigger_num = nums2[j]
                    break
            ans.append(bigger_num)
        return ans
    # Time: O(n+m)

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None

        mapping = {}
        result = []
        stack = []
        stack.append(nums2[0])

        for i in range(1, len(nums2)):
            # if stack is not empty, then compare it's last element with nums2[i]
            while stack and nums2[i] > stack[-1]:
                # if the new element is greater than stack's top element, then add this to dictionary
                mapping[stack[-1]] = nums2[i]
                # since we found a pair for the top element, remove it.
                stack.pop()
            # add the element nums2[i] to the stack because we need to find a number greater than this
            stack.append(nums2[i])

        # if there are elements in the stack for which we didn't find a greater number, map them to -1
        for element in stack:
            mapping[element] = -1

        for i in range(len(nums1)):
            result.append(mapping[nums1[i]])
        return result
