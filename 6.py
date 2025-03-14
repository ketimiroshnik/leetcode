#283. Move Zeroes

def moveZeroes(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    last_good = -1
    count_null = 0
    for i in range(n):
        if nums[i] != 0:
            nums[last_good + 1] = nums[i]
            last_good += 1
        else:
            count_null += 1
    for i in range(n - count_null, n):
        nums[i] = 0

