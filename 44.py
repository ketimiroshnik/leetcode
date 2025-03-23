# 1446. Consecutive Characters

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 1
        now = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                now += 1
                ans = max(ans, now)
            else:
                now = 1
        return ans
