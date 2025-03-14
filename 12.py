# 20. Valid Parentheses
from collections import deque

def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = deque()
    d = {']': '[', ')': '(', '}': '{'}

    for e in s:
        if e in '([{':
            stack.append(e)
        else:
            if not stack:
                return False
            elif stack.pop() != d[e]:
                return False
    if not stack:
        return True
    else:
        return False


