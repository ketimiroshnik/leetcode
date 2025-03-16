# 523. Continuous Subarray Sum


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        A good subarray is a subarray where:
        its length is at least two, and
        the sum of the elements of the subarray is a multiple of k.
        """
        rests = set()
        before = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if (s % k) in rests:
                return True
            rests.add(before % k)
            before = s
        return False


s = Solution()
print(s.checkSubarraySum([23,2,4,6,7], 6))

