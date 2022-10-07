from collections import Counter


class MyCalendarThree:

    def __init__(self):
        self.diff = {}
        self.vals = Counter()
        self.lazy = Counter()

    def book(self, start: int, end: int) -> int:
        # return self.book1(start, end)
        return self.book2(start, end)

    # Sweep-line algorithm. Time: O(n**2)
    def book1(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        ans = 0
        curr = 0
        for t in sorted(self.diff.keys()):
            curr += self.diff[t]
            ans = max(ans, curr)
        return ans

    # Segment Tree. Time: O(n log C). C = Max time (i.e. 10**9)
    def book2(self, start: int, end: int) -> int:

        def update(start: int,
                   end: int,
                   left: int = 0,
                   right: int = 10**9,
                   idx: int = 1) -> None:
            if start > right or end < left:
                return

            if start <= left <= right <= end:
                self.vals[idx] += 1
                self.lazy[idx] += 1
            else:
                mid = (left + right) // 2
                update(start, end, left, mid, idx * 2)
                update(start, end, mid + 1, right, idx * 2 + 1)
                self.vals[idx] = self.lazy[idx] + \
                    max(self.vals[2*idx], self.vals[2*idx+1])

        update(start, end - 1)
        return self.vals[1]


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

myCalendarThree = MyCalendarThree()
print(myCalendarThree.book(10, 20))
print(myCalendarThree.book(50, 60))
print(myCalendarThree.book(10, 40))
print(myCalendarThree.book(5, 15))
print(myCalendarThree.book(5, 10))
print(myCalendarThree.book(25, 55))
