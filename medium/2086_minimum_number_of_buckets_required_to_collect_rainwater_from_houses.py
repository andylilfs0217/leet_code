class Solution:
    def minimumBuckets(self, street: str) -> int:
        # Filter out HHH
        street_len = len(street)
        for i, pos in enumerate(street):
            have_space = True
            if i == 0 and pos == 'H' and i + 1 < street_len and street[i + 1] == 'H':
                have_space = False
            elif i == street_len - 1 and pos == 'H' and i - 1 >= 0 and street[i - 1] == 'H':
                have_space = False
            else:
                have_space = pos == '.' or street[i -
                                                  1] == '.' or street[i+1] == '.'
            return have_space
