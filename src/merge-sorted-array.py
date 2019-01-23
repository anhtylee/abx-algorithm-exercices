# url https://leetcode.com/problems/merge-sorted-array/
# writtenby:anhty9le


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i = 0
        lenN = n1 = len(nums1)

        while i < lenN - m:
            print(i, n1)
            nums1.pop(n1 - 1)
            n1 -= 1
            i += 1

        for i in range(n):
            nums1.append(nums2[i])

        nums1.sort()
