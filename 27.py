# 279. Perfect Squares

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [] # это все возможные квадраты
        x = 1
        x_2 = 1
        while x_2 <= n:
            squares.append(x_2)
            x += 1
            x_2 = x * x
        # пусть count[i] - это наименьшее число слагаемых чтобы собрать сумму i
        # сделаем динамику по i
        count = [-1] * (n + 1)
        count[0] = 0
        count[1] = 1
        for i in range(2, n + 1):
            res = i
            for sq in squares:
                if (sq > i):
                    break
                res = min(count[i - sq] + 1, res)
            count[i] = res
        return count[n]



s = Solution()
print(s.numSquares(13))



