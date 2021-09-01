import queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mainQueue = queue.Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        tempQueue = queue.Queue()
        tempQueue.put_nowait(x)
        while not self.mainQueue.empty():
            tempQueue.put_nowait(self.mainQueue.get_nowait())
        self.mainQueue = tempQueue

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.mainQueue.get_nowait()

    def top(self) -> int:
        """
        Get the top element.
        """
        res = self.mainQueue.get_nowait()
        self.push(res)
        return res

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.mainQueue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
