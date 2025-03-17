# 350. Intersection of Two Arrays II


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Given two integer arrays nums1 and nums2, return an array of their intersection.
        Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
        """
        nums1.sort()
        nums2.sort()
        res = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res

