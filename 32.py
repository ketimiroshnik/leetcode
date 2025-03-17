# 150. Evaluate Reverse Polish Notation

from collections import deque


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = deque()
        operations = ['+', '-', '*', '/']
        for e in tokens:
            if e in operations:
                second = stack.pop()
                first = stack.pop()
                res = -1
                if e == '+':
                    res = first + second
                elif e == "-":
                    res = first - second
                elif e == "*":
                    res = first * second
                elif e == "/":
                    res = int(float(first / second))
                stack.append(res)
            else:
                stack.append(int(e))
        return stack.pop()





s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))