# 341. Flatten Nested List Iterator


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        self.list = nestedList
        self.index = 0
        self.iter = None
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """

    def next(self):
        """
        :rtype: int
        """
        if self.iter:
            if self.iter.hasNext():
                return self.iter.next()
            else:
                self.iter = None
                self.index += 1

        while True:
            if self.list[self.index].isInteger():
                self.index += 1
                return self.list[self.index-1].getInteger()

            other_list = self.list[self.index].getList()
            self.iter = NestedIterator(other_list)
            if self.iter.hasNext():
                return self.iter.next()
            # если список пуст, то заново
            self.iter = None
            self.index += 1

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.iter:
            if self.iter.hasNext():
                return True
            else:
                self.iter = None
                self.index += 1

        while self.index < len(self.list):
            if self.list[self.index].isInteger():
                return True

            other_list = self.list[self.index].getList()
            self.iter = NestedIterator(other_list)
            if self.iter.hasNext():
                return True
            self.iter = None
            # если список пуст, то заново
            self.index += 1
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())