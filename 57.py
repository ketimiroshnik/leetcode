"""
Можно ли убрать один символ из строки, чтобы она стала палиндромом?
"""

def solve(s):
    """
        :type s: string
        :rtype: bool
    """
    def is_palindrome(t):
        for index in range(len(t) // 2):
            if t[index] != t[-index-1]:
                return False
            return True
    n = len(s)
    l = 0
    r = n - 1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        # несовпадение
        # проверить палиндромность от l+1 до r (включительно) и от l до r-1 (включительно)
        return is_palindrome(s[l:r]) or is_palindrome(s[l+1:r+1])
    # если мы оказались здесь, то строка и так быда палиндромом


s = "1_2344321"
print(solve(s))
