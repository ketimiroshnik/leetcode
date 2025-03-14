#49. Group Anagrams

from collections import defaultdict

class Solution(object):
    def coding(self, s):
        """
        :param s: string of latin symbols
        :return: string: символ в сллве + частота в алфавитном порядке
        """
        count = [0] * 26
        for e in s:
            count[ord(e) - ord('a')] += 1
        res = []
        for i in range(26):
            if count[i] > 0:
                res.append(chr(ord('a') + i))
                res.append(str(count[i]))
        return ''.join(res)


    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        for e in strs:
            d[self.coding(e)].append(e)
        ans = []
        ans.extend(d.values())
        return ans


strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print(s.groupAnagrams(strs))
