# 392. Is Subsequence

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
        """
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        n_s = len(s)
        n_t = len(t)
        count = 0
        for i in range(n_t):
            if t[i] == s[count]:
                count += 1
            if count == n_s:
                return True

        return False


s = Solution()
print(s.isSubsequence("abc",  "ahbgdc"))


