# 1493. Longest Subarray of 1's After Deleting One Element

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        start = 0
        count_null = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                count_null += 1
            if count_null > 1:
                if nums[start] == 0:
                    count_null -= 1
                start += 1
        return len(nums) - start - 1




