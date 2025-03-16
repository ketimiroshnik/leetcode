# 415. Add Strings

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ""
        add = False
        n1 = len(num1)
        n2 = len(num2)
        i = n1 - 1
        j = n2 - 1
        while i >= 0 or j >= 0:
            if i < 0:
                d1 = 0
            else:
                d1 = int(num1[i])
            if j < 0:
                d2 = 0
            else:
                d2 = int(num2[j])
            s = d1 + d2 + add
            ans = str(s % 10) + ans
            if s >= 10:
                add = True
            else:
                add = False
            i -= 1
            j -= 1

        if add:
            ans = '1' + ans
        return ans


s = Solution()
print(s.addStrings('12', '456'))
