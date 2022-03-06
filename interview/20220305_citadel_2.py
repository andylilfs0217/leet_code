#!/bin/python3

from collections import Counter
import math
import os
import random
import re
import sys
from typing import List


#
# Complete the 'stockPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY stocksProfit
#  2. LONG_INTEGER target
#

def stockPairs(stocksProfit: List[int], target: int) -> int:
    # Write your code here
    counter = Counter(stocksProfit)
    keys = list(counter.keys())
    visited = {}
    for key in keys:
        visited[key] = False
    ans = 0
    for key in keys:
        stock1 = key
        stock2 = target - key
        if stock2 not in counter or visited[stock1]:
            continue
        counter[stock1] -= 1
        counter[stock2] -= 1
        if counter[stock1] >= 0 and counter[stock2] >= 0:
            ans += 1
            visited[stock1] = True
            visited[stock2] = True
        counter[stock1] += 1
        counter[stock2] += 1
    return ans


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     stocksProfit_count = int(input().strip())

#     stocksProfit = []

#     for _ in range(stocksProfit_count):
#         stocksProfit_item = int(input().strip())
#         stocksProfit.append(stocksProfit_item)

#     target = int(input().strip())

#     result = stockPairs(stocksProfit, target)

#     fptr.write(str(result) + '\n')

#     fptr.close()

print(stockPairs([6, 1, 3, 46, 1, 3, 9, ], 47))
