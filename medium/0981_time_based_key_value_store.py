class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        v_list = self.hm.get(key, [])
        v_list.append((timestamp, value))
        self.hm[key] = v_list

    def get(self, key: str, timestamp: int) -> str:
        v_list = self.hm.get(key, [])
        n = len(v_list)
        # Linear search
        # ans = ""
        # for i in range(n):
        #     t, value = v_list[i]
        #     if timestamp >= t:
        #         ans = value
        #     else:
        #         break
        # return ans

        # Binary search
        ans = ""
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            t1, value1 = v_list[m]
            if m + 1 >= n:
                if timestamp >= t1:
                    ans = value1
                break
            else:
                t2, _ = v_list[m + 1]
                if timestamp >= t1 and timestamp < t2:
                    ans = value1
                    break
                elif timestamp >= t1:
                    l = m + 1
                else:
                    r = m - 1
                pass
        return ans


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
timeMap.set("foo", "bar3", 7)
print(timeMap.get("foo", 8))
print(timeMap.get("foo", 5))
print(timeMap.get("foo", 2))
print(timeMap.get("foo", 0))
print(timeMap.get("bar", 3))