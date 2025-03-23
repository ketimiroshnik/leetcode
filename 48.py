# 3. Longest Substring Without Repeating Characters


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # d[e] - самый крайний индекс на котором встретился элемент e
        d = dict()
        start_i = 0 # индекс с которого мы сейчас считаем валидную строку
        ans = 0
        for i in range(len(s)):
            if s[i] not in d or d[s[i]] < start_i:
                # s[i] еще не встречалось либо оно встречалось еще до точки отсчета
                d[s[i]] = i
            else:
                # s[i] встретилось где-то в области нашего отсчета
                # значит сохраним текущий результат и передвинем наш старт
                ans = max(ans, i - start_i)
                start_i = d[s[i]] + 1
                d[s[i]] = i
        ans = max(ans, len(s) - start_i)

        return ans


s = Solution()
print(s.lengthOfLongestSubstring("abba"))