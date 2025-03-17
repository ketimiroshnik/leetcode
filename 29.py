# 977. Squares of a Sorted Array


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # краевые случаи чтоб не думать о них
        if nums[0] >= 0:
            return [e ** 2 for e in nums]
        if nums[-1] <= 0:
            return [e ** 2 for e in nums][::-1]

        start_pos = 0  # индекс с кот начинаются положительные
        while nums[start_pos] < 0:
            start_pos += 1

        ans = []
        ind_pos = start_pos
        ind_neg = start_pos - 1
        last_pos = len(nums) - 1
        first_neg = 0

        while ind_pos <= last_pos or ind_neg >= first_neg:
            if (ind_pos > last_pos):
                while ind_neg >= first_neg:
                    ans.append(nums[ind_neg] ** 2)
                    ind_neg -= 1
                break
            elif ind_neg < first_neg:
                while ind_pos <= last_pos:
                    ans.append(nums[ind_pos] ** 2)
                    ind_pos += 1
                break

            if abs(nums[ind_pos]) < abs(nums[ind_neg]):
                ans.append(nums[ind_pos] ** 2)
                ind_pos += 1
            else:
                ans.append(nums[ind_neg] ** 2)
                ind_neg -= 1
        return ans



s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))

