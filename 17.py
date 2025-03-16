# 557. Reverse Words in a String III


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = [e[::-1] for e in s.split()]
        return ' '.join(words)

