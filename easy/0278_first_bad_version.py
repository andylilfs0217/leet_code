# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(bad: int) -> int:
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start != end:
            mid = (start+end) // 2
            isBad = isBadVersion(mid)
            if isBad:
                end = mid
            else:
                start = mid + 1
        return start
