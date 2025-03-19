# 232. Implement Queue using Stacks

from collections import deque


class MyQueue(object):

    def __init__(self):
        self.first = deque()
        self.second = deque()
        # ------|  |------
        # ______|  |______
        #

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.first.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while self.first:
            self.second.append(self.first.pop())
        return self.second.pop()

    def peek(self):
        """
        :rtype: int
        """
        while self.first:
            self.second.append(self.first.pop())
        return self.second[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.first and not self.second

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()