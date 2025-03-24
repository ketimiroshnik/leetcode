# 281. Zigzag Iterator

"""
Обобщение на k векторов
Given k 1d vectors, implement an iterator to return their elements alternately.
"""

class ZigzagIterator(object):

    def __init__(self, v):
        """
        Initialize your data structure here.
        :type v: List[List[int]]
        """
        self.vec = v
        self.i_vec = 0 # индекс текущего вектора
        self.n_vec = len(self.vec)
        self.indexes = [0] * self.n_vec # индекс следующего элемента для этого вектора



    def next(self):
        """
        :rtype: int
        """
        stated_i_vec = self.i_vec
        while True:
            if self.indexes[self.i_vec] < len(self.vec[self.i_vec]):
                # this vector is ok
                value = self.vec[self.i_vec][self.indexes[self.i_vec]]
                self.indexes[self.i_vec] += 1 # сдвигаем индекс внутри текущего вектора
                self.i_vec = (self.i_vec + 1) % self.n_vec # переключаемся на следуюший вектор
                return value
            # this vector is ended
            self.i_vec = (self.i_vec + 1) % self.n_vec
            if self.i_vec == stated_i_vec:
                # сделали круг и ничего не нашли
                return None


    def hasNext(self):
        """
        :rtype: bool
        """
        stated_i_vec = self.i_vec
        while True:
            if self.indexes[self.i_vec] < len(self.vec[self.i_vec]):
                # this vector is ok
                return True
            # this vector is ended
            self.i_vec = (self.i_vec + 1) % self.n_vec
            if self.i_vec == stated_i_vec:
                # сделали круг и ничего не нашли
                return False




v1 = [1,4]
v2 = [2,5,7,9]
v3 = [3,6,8]


zigzag = ZigzagIterator([v1, v2, v3])

while zigzag.hasNext():
    print(zigzag.next())
