class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack = []
        for d in dirs:
            if d == '..':
                if len(stack) > 0:
                    stack.pop()
            elif d == '.' or d == '':
                continue
            else:
                stack.append(d)
        return '/' + '/'.join(stack)
