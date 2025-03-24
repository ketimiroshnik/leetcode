# 438. Find All Anagrams in a String



class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        d_p = [0] * 26
        for e in p:
            d_p[ord(e) - ord('a')] += 1

        ans = []
        d_s = [0] * 26
        # окно размером len(p)
        for i in range(len(s)):
            if i < len(p) - 1:
                d_s[ord(s[i]) - ord('a')] += 1
                continue
            if i > len(p) - 1:
                d_s[ord(s[i - len(p)]) - ord('a')] -= 1
            d_s[ord(s[i]) - ord('a')] += 1

            okey = True
            for j in range(26):
                if d_p[j] != d_s[j]:
                    okey = False
                    break
            if okey:
                ans.append(i - len(p) + 1)
        return ans


s = Solution()

print(s.findAnagrams("cbaebabacd", "abc"))


