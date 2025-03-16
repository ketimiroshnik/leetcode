# 387. First Unique Character in a String

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        mas = [n] * 26
        # n не было такого символа
        # n+1 был более одного раза
        # >=0 один раз ровно
        for i in range(len(s)):
            e = s[i]
            code = ord(e) - ord('a')
            if mas[code] == n:
                mas[code] = i
            else:
                mas[code] = n+1
        ans = min(mas)
        if ans >= n:
            return -1
        return ans

