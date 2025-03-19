# 88. Merge Sorted Array

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        w = m + n - 1
        while i >= 0 or j >= 0:
            if i < 0:
                nums1[w] = nums2[j]
                w -= 1
                j -= 1
                continue
            if j < 0:
                nums1[w] = nums1[i]
                w -= 1
                i -= 1
                continue

            if nums1[i] > nums2[j]:
                nums1[w] = nums1[i]
                w -= 1
                i -= 1
            else:
                nums1[w] = nums2[j]
                w -= 1
                j -= 1



