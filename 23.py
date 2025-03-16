# 26. Remove Duplicates from Sorted Array


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        last_good = -1
        for i in range(n):
            if (i == 0) or (nums[last_good] != nums[i]):
                last_good += 1
                nums[last_good] = nums[i]
        return last_good + 1

