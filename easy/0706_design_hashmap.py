class MyHashMap:
    def eval_hash(self, key: int) -> int:
        return ((key*1031237) & (1 << 20) - 1) >> 5

    def __init__(self):
        self.arr = [[] for _ in range(1 << 15)]

    def put(self, key: int, value: int) -> None:
        t = self.eval_hash(key)
        for i in self.arr[t]:
            if i[0] == key:
                i[1] = value
                return
        self.arr[t].append([key, value])

    def get(self, key: int) -> int:
        t = self.eval_hash(key)
        for i in self.arr[t]:
            if i[0] == key:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        for i in self.arr[t]:
            if i[0] == key:
                self.arr[t].remove(i)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
