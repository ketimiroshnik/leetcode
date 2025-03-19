# 771. Jewels and Stones


from collections import defaultdict

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        d = set(list(jewels))
        ans = 0
        for e in stones:
            if e in d:
                ans += 1
        return ans
