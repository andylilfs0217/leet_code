class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        n, i, count = len(street), 0, 0
        while i < n:
            if street[i] == 'H' and i + 1 < n and street[i + 1] == '.' and ((i - 1 >= 0 and street[i - 1] != 'B') or i - 1 < 0):
                street[i + 1] = 'B'
            elif street[i] == 'H' and i - 1 >= 0 and street[i - 1] == '.':
                street[i - 1] = 'B'
            elif street[i] == 'H' and (i + 1 >= n or street[i + 1] == 'H') and (i - 1 < 0 or street[i - 1] == 'H'):
                return -1
            i += 1
        return street.count('B')
