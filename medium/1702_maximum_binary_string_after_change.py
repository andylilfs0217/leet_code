class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        result = list(binary)
        curr = 0
        while curr < len(result) and result[curr] == '1':
            curr += 1
        if curr == len(result):
            return ''.join(result)
        num_of_one = 0
        while curr < len(result):
            if result[curr] == '1':
                num_of_one += 1
            else:
                result[curr] = '1'
            curr += 1
        result[len(result) - 1 - num_of_one] = '0'
        return ''.join(result)
