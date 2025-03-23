# 986. Interval List Intersections


class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """

        i = 0
        j = 0
        n1 = len(firstList)
        n2 = len(secondList)
        ans = []
        while i < n1 and j < n2:
            s1, e1 = tuple(firstList[i])
            s2, e2 = tuple(secondList[j])

            if e1 < s2:
                i += 1
                continue
            if e2 < s1:
                j += 1
                continue

            s = max(s1, s2)
            e = min(e1, e2)
            ans.append([s, e])
            if e2 > e1:
                i += 1
            else:
                j += 1
        return ans



s = Solution()
firstList = [[1,3],[5,9]]
secondList = []
print(s.intervalIntersection(firstList, secondList))

