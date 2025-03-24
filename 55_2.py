# 161. One Edit Distance


"""
Given two strings s and t, determine if they are both one edit distance apart.

Note:
There are 3 possiblities to satisify one edit distance apart:
Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
"""

class Solution(object):
    def isOneEditDistance(self, s, t):
        if len(s) < len(t):
            s, t = t, s

        if len(s) - len(t) > 1:
            return False

        for i in range(len(t)):
            if t[i] == s[i]:
                continue
            if len(s) == len(t):
                # если это был последний символ, то как раз его нужно заменить
                # если не последний, то должны совпадать все символы после i
                return (i == len(t) - 1) or (t[i+1:] == s[i+1:])
            else:
                # скип s[i] и хвосты должны совпасть
                return t[i:] == s[i+1:]
        return len(s) != len(t)


sol = Solution()

s = "12_3"
t = "1213"
print(sol.isOneEditDistance(s, t))








