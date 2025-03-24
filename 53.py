# 487 Max Consecutive Ones II

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :param nums: List[int]
        :return: int

        Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
        """
        count_null = 0
        start = 0
        for end in len(nums):
            if nums[end] == 0:
                count_null += 1
            if count_null > 1:
                start += 1
                if nums[start - 1] == 0:
                    count_null -= 1
        return len(nums) - start