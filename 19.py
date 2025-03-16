# 238. Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pref_products = [0] * n
        suf_products = [0] * n
        s = 1
        for i in range(n):
            s *= nums[i]
            pref_products[i] = s
        s = 1
        for i in range(n - 1, -1, -1):
            s *= nums[i]
            suf_products[i] = s
        suf_products.append(1)
        pref_products.append(1)
        answer = []
        for i in range(n):
            print(i, pref_products[i - 1], suf_products[i + 1])
            x = pref_products[i - 1] * suf_products[i + 1]
            answer.append(x)
        return answer


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
