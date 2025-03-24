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
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) < len(t):
            s, t = t, s
        # инвариант: len(s) >= len(t)
        left_s = -1
        left_t = -1
        right_s = len(s)
        right_t = len(t)
        while (left_t + 1 < len(t) and left_s + 1 < len(s)) and s[left_s + 1] == t[left_t + 1]:
            left_s += 1
            left_t += 1
        while (right_t -1 >= 0 and right_s - 1 >= 0) and s[right_s - 1] == t[right_t - 1]:
            right_s -= 1
            right_t -= 1
        # совпадают s[:left_s + 1] == t[:left_t + 1] and s[right_s:] == t[right_t:]
        suit = (left_s + 1) + (len(s) - right_s)  # кол-во совпавших символов
        if suit == len(s) - 1:
            return True
        return False


sol = Solution()

s = "1213"
t = "1213"
print(sol.isOneEditDistance(s, t))








