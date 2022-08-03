# Brute force
class MyCalendar:

    def __init__(self):
        self.cal = []  # (start, end)

    def book(self, start: int, end: int) -> bool:
        for s, e in self.cal:
            if s < end and start < e:
                return False
        self.cal.append((start, end))
        return True


# Binary search tree
class Node:
    __slots__ = 'start', 'end', 'left', 'right'

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False


class MyCalendar():
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


obj = MyCalendar()
print(obj.book(10, 20) == True)
print(obj.book(15, 25) == False)
print(obj.book(20, 30) == True)

obj = MyCalendar()
print(obj.book(47, 50) == True)
print(obj.book(33, 41) == True)
print(obj.book(39, 45) == False)
print(obj.book(33, 42) == False)
print(obj.book(25, 32) == True)
print(obj.book(26, 35) == False)
print(obj.book(19, 25) == True)
print(obj.book(3, 8) == True)
print(obj.book(8, 13) == True)
print(obj.book(18, 27) == False)
