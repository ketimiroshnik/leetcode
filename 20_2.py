# 763. Partition Labels


from collections import defaultdict
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        n = len(s)
        count_s = [0] * 26
        for i in range(n):
            value = ord(s[i]) - ord('a')
            count_s[value] += 1

        len_groups = []
        count_window = defaultdict(int)
        start_group = 0
        for i in range(n):
            value = ord(s[i]) - ord('a')
            count_window[value] += 1

            okey = True
            for key, value in count_window.items():
                if value != count_s[key]:
                    okey = False
                    break
            if okey:
                len_groups.append(i - start_group + 1)
                count_window = defaultdict(int)
                start_group = i + 1
        return len_groups




