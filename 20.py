# 763. Partition Labels

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        starts = [-1] * 26
        ends = [-1] * 26
        for i in range(n):
            value = ord(s[i]) - ord('a')
            if starts[value] == -1:
                starts[value] = i
            ends[value] = i

        segments = []
        for i in range(26):
            if starts[i] != -1:
                segments.append((starts[i], ends[i]))
        segments.sort()

        len_groups = []
        start_group = 0
        end_group = 0

        for seg in segments:
            start, end = seg
            if start <= end_group:
                end_group = max(end_group, end)
            else:
                len_groups.append(end_group - start_group + 1)
                start_group, end_group = start, end
        len_groups.append(end_group - start_group + 1)
        return len_groups



s = Solution()
print(s.partitionLabels("eccbbbbdec"))


