# 159 Longest Substring with At Most Two Distinct Characters

from collections import defaultdict, Counter

def solution(s):
    d = defaultdict(int)
    start = 0
    ans = 0
    for i in range(len(s)):
        d[s[i]] += 1
        while len(d) > 2:
            d[s[start]] -= 1
            if d[s[start]] == 0:
                d.pop(s[start])
            start += 1
        ans = max(ans, i - start + 1)
    return ans






# print(solution2("ccaabbb"))

check()


