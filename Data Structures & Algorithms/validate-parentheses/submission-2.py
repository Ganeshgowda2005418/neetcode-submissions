class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0