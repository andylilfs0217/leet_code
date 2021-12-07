class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.curr_idx = 0

    def visit(self, url: str) -> None:
        self.stack = self.stack[0:self.curr_idx+1]
        self.stack.append(url)
        self.curr_idx += 1

    def back(self, steps: int) -> str:
        self.curr_idx -= steps
        if self.curr_idx < 0:
            self.curr_idx = 0
        return self.stack[self.curr_idx]

    def forward(self, steps: int) -> str:
        self.curr_idx += steps
        if self.curr_idx+1 > len(self.stack):
            self.curr_idx = len(self.stack) - 1
        return self.stack[self.curr_idx]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
