import collections
from io import TextIOWrapper
from typing import List


def Solution(f: TextIOWrapper):
    lines = f.read().splitlines()

    # Write your codes here
    def getBingoMap(lines: List[str]) -> collections.defaultdict:
        bingo = [line.split() for line in lines]
        bingo_map = collections.defaultdict(list)
        for i, row in enumerate(bingo):
            for j, cell in enumerate(row):
                bingo_map[cell] = [i, j, False]
        return bingo_map

    def checkBingo(bingo: collections.defaultdict) -> bool:
        marked = []
        for _, v in bingo.items():
            if v[2]:
                marked.append(v[:2])
        if len(marked) == 0:
            return False
        # Check horizontal or vertical
        h_counter, v_counter = [
            collections.Counter(x) for x in list(zip(*marked))
        ]
        h_max_count, v_max_count = max(h_counter.values()), max(
            v_counter.values())
        if h_max_count >= 5 or v_max_count >= 5:
            return True
        return False

    def getResult(bingo: collections.defaultdict, call: str) -> int:
        unmarked_sum = 0
        for k, v in bingo.items():
            if not v[2]:
                unmarked_sum += int(k)
        call_int = int(call)
        res = unmarked_sum * call_int
        return res

    res = 0
    calls = lines[0].split(',')
    bingos: List[collections.defaultdict] = []
    l, r = 2, 2
    while l < len(lines) and r < len(lines):
        if len(lines[r]) == 0:
            bingo_map = getBingoMap(lines[l:r])
            bingos.append(bingo_map)
            l = r + 1
        r += 1
    bingo_map = getBingoMap(lines[l:r])
    bingos.append(bingo_map)

    for i, call in enumerate(calls):
        print(call)
        next_bingos = []
        for bingo in bingos:
            if call in bingo:
                bingo[call][2] = True
            if i >= 4:
                isBingo = checkBingo(bingo)
                if not isBingo:
                    next_bingos.append(bingo)
        if i >= 4:
            if len(next_bingos) > 0:
                bingos = next_bingos
            else:
                res = getResult(bingo, call)
                break

    # Finish your codes here
    return res
