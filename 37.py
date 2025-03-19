# 5. Longest Palindromic Substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        consist of only digits and English letters.
        """
        n = len(s)
        ans = 1
        ans_s = s[0]
        for center in range(n):
            # нечетная длина
            now = 1
            i = 1
            while True:
                if (center + i) >= n or (center - i) < 0:
                    break
                if s[center - i] == s[center + i]:
                    now += 2
                else:
                    break
                i += 1
            if now > ans:
                ans_s = s[center - i + 1: center + i]
                ans = now

            center1, center2 = center, center + 1
            now = 0
            i = 0
            while True:
                if (center2 + i) >= n or (center1 - i) < 0:
                    break
                if s[center1 - i] == s[center2 + i]:
                    now += 2
                else:
                    break
                i += 1
            if now > ans:
                ans_s = s[center1 - i + 1: center2 + i]
                ans = now
        return ans_s


s = Solution()
print(s.longestPalindrome("ccc"))







