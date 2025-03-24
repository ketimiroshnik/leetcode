# 1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        was = set()
        d = dict()
        for i in range(len(nums)):
            x = nums[i]
            if (target - x) in was:
                return [d[target - x], i]

            if x not in was:
                d[x] = i
                was.add(x)
                
