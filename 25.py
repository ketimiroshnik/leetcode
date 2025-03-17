# 33. Search in Rotated Sorted Array

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_start(nums):
            n = len(nums)
            l = 0
            r = n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < nums[(m + 1) % n] and nums[m] < nums[(m - 1) % n]:
                    return m
                if nums[m] >= nums[0]:
                    l = m + 1
                else:
                    r = m
            return 0

        start = find_start(nums)
        print(start)
        n = len(nums)
        if target < nums[start] or target > nums[(start + n-1) % n]:
            return -1

        l = 0
        r = n
        while l < r:
            m = (l + r) // 2
            if nums[(m + start) % n] == target:
                return (m + start) % n
            if nums[(m + start) % n] < target:
                l = m + 1
            else:
                r = m
        return -1


s = Solution()
nums = [1]
print(s.search(nums, 0))
