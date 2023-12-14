class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = list()
        for chr in s:
            if chr == '(':
                stack.append(1)
            elif chr == '{':
                stack.append(2)
            elif chr == '[':
                stack.append(3)
            elif chr == ')':
                if len(stack) > 0 and stack[-1] == 1:
                    stack.pop(-1)
                else:
                    return False
            elif chr == '}':
                if len(stack) > 0 and stack[-1] == 2:
                    stack.pop(-1)
                else:
                    return False
            elif chr == ']':
                if len(stack) > 0 and stack[-1] == 3:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0
