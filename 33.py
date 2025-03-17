# 268. Missing Number


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        solution using only O(1) extra space complexity and O(n) runtime complexity
        """
        max_elem = max(nums)
        real_s = sum(nums)
        need_s = max_elem * (max_elem + 1) / 2
        elem = int(need_s - real_s)
        if elem == 0 and 0 in nums:
            return max_elem + 1
        return elem



s = Solution()
print(s.missingNumber([3,0,1]))
print(s.missingNumber([0, 1]))