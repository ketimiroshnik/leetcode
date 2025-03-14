#125. Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        if len(s) == 1:
            return True

        a = 0
        b = len(s) - 1
        while b > a:
            if not s[a].isalnum():
                a += 1
                continue
            if not s[b].isalnum():
                b -= 1
                continue
            if s[a].lower() != s[b].lower():
                return False
            a += 1
            b -= 1
        return True


print(ord('a'), ord('z'))
s = "dsa"
s.isalnum()