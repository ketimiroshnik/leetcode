# 567. Permutation in String

def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool

    In other words, return true if one of s1's permutations is the substring of s2.
    every simbol of s1 must be in s2
    """
    if len(s2) < len(s1):
        return False
    k = len(s1)
    d_s1 = [0] * 26
    d_s2 = [0] * 26
    for i in range(26):
        d_s1[i] = 0
        d_s2[i] = 0
    for e in s1:
        d_s1[ord(e) - ord('a')] += 1
    for e in s2[:k]:
        d_s2[ord(e) - ord('a')] += 1
    if d_s1 == d_s2:
        return True
    for i in range(k, len(s2)):
        d_s2[ord(s2[i-k]) - ord('a')] -= 1
        d_s2[ord(s2[i]) - ord('a')] += 1
        if d_s1 == d_s2:
            return True
    return False


s1 = "adc"
s2 = "dcda"

print(checkInclusion(s1, s2))