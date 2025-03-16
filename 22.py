# 153. Find Minimum in Rotated Sorted Array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        l = 0
        r = n - 1
        while (l <= r):
            m = (l + r) // 2
            if nums[m] < nums[(m + 1) % n] and nums[m] < nums[(m - 1) % n]:
                return nums[m]
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m
        return nums[0]


s = Solution()
nums = [17]

print(s.findMin(nums))