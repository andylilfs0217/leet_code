#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys
from typing import List


#
# Complete the 'hackerCards' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY collection
#  2. INTEGER d
#

def hackerCards(collection: List[int], d: int) -> List[int]:
    counter = Counter(collection)
    min_num = 1
    ans = []
    keys = list(counter.keys())
    keys.sort()
    for num in keys:
        l = min_num
        r = num - 1
        sub_sum = findSum(l, r)
        if num > d:
            break
        if 0 < sub_sum <= d:
            for i in range(l, r+1):
                ans.append(i)
            d -= sub_sum
        elif sub_sum > d:
            while l <= d:
                ans.append(l)
                l += 1
                d -= l
        min_num = num + 1
    while min_num <= d:
        ans.append(min_num)
        d -= min_num
        min_num = min_num + 1
    return ans


def findSum(l, r):
    return (l + r) * (r - l + 1) // 2


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     collection_count = int(input().strip())

#     collection = []

#     for _ in range(collection_count):
#         collection_item = int(input().strip())
#         collection.append(collection_item)

#     d = int(input().strip())

#     result = hackerCards(collection, d)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()


print(hackerCards([6917, 14711, 23047, 28434, 28927,
      35577, 36999, 39362, 39390, 48081], 10459))
