# 1493. Longest Subarray of 1's After Deleting One Element

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        ans = 0
        count_null = 0
        last_null = -1
        len_now = 0
        for i in range(len(nums)):
            e = nums[i]
            if (e == 1):
                len_now += 1
                ans = max(ans, len_now)
                continue
            if (count_null == 0):
                last_null = i
                count_null += 1
                len_now += 1
                ans = max(ans, len_now)
            else:
                count_null = 1
                len_now = i - last_null
                ans = max(ans, len_now)
                last_null = i
        return ans - 1


s = Solution()
print(s.longestSubarray([1,1]))


