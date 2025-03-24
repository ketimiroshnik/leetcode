# 56. Merge Intervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        ans = []
        s0 = intervals[0][0]
        e0 = intervals[0][1]
        for elem in intervals[1:]:
            # s0 <= s1
            s1, e1 = tuple(elem)
            if e0 < s1:
                # s0 e0 s1 e1
                ans.append([s0, e0])
                s0, e0 = s1, e1
            elif e0 < e1:
                # s0 s1 e0 e1
                e0 = e1
            elif e0 > e1:
                # s0 s1 e1 e0
                pass
        ans.append([s0, e0])
        return ans

intervals = [[1,4],[4,5]]

s = Solution()

print(s.merge(intervals))