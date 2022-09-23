from collections import Counter
from typing import List


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        return self.leastInterval1(tasks, n)

    def leastInterval1(self, tasks: List[str], n: int) -> int:
        # tasks = ["A","A","A","B","B","B"]
        # n = 2

        counts = list(Counter(tasks).values())  # [3,3]
        max_count = max(counts)  # 3
        num_of_chars_with_max_count = counts.count(max_count)  # 2, A and B

        num_of_chunks_with_idles = max_count - 1  # 2  -> A  A  A

        # either a task will fill an empty place or the place stays idle,
        # either way the chunk size stays the same
        length_of_a_chunk_with_idle = n + 1  # 3 -> A _ _ A _ _ A

        # on the final chunk, there will only be most frequent letters
        length_of_the_final_chunk = num_of_chars_with_max_count  # 2

        length_of_all_chunks = (num_of_chunks_with_idles *
                                length_of_a_chunk_with_idle
                                ) + length_of_the_final_chunk  # 2*3 + 2 = 8
        # -> A B _ A B _ A B

        res = max(len(tasks), length_of_all_chunks)
        return res


print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 8)
print(Solution().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0) == 6)
print(Solution().leastInterval(
    tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=16)
      == 6)
