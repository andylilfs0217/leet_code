import collections
from typing import List
from bisect import bisect_left


class TimeMap:

    def __init__(self):
        """
        {
            'foo': [(1, 'bar'), (4, 'bar2'), (7, 'bar3')]
        }
        """
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        def search_val_from_list(ts: int, val_list: List) -> str:
            res = ""
            n = len(val_list)
            l, r = 0, n - 1
            found_res = False
            while l <= r and not found_res:
                mid = (l + r) // 2
                t, val = val_list[mid]
                if t == ts:
                    res = val
                    found_res = True
                elif t < ts:
                    res = val
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        val_hist = self.time_map[key]
        res = search_val_from_list(timestamp, val_hist)
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))  # bar
print(timeMap.get("foo", 3))  # bar
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))  # bar2
print(timeMap.get("foo", 5))  # bar2
timeMap.set("foo", "bar3", 7)
print(timeMap.get("foo", 8))  # bar3
print(timeMap.get("foo", 5))  # bar2
print(timeMap.get("foo", 2))  # bar
print(timeMap.get("foo", 0))  # ''
print(timeMap.get("bar", 3))  # ''
