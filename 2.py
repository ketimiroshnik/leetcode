#228. Summary Ranges

class Solution(object):
    def summaryRanges(self, nums):

        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        first = None
        last = -1
        for e in nums:
            if first is None:
                first = e
                last = e
            elif last + 1 != e:
                #res.append(f"{first}->{last}")
                if first == last:
                    res.append(str(first))
                else:
                    res.append(str(first) + "->" + str(last))
                first = e
                last = e
            else:
                last += 1
        if first == last:
            res.append(str(first))
        else:
            res.append(str(first) + "->" + str(last))
        return res


nums = [0,1,2,4,5,7]
s = Solution()
print(s.summaryRanges(nums))