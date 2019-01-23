# url https://leetcode.com/problems/intersection-of-two-arrays/
# writtenby:anhty9le


def fixNums(nums):
    nums.sort()
    i = 0
    n = len(nums)

    while i < n - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
            n -= 1
            i -= 1
        i += 1

    return nums


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        arr1 = fixNums(nums1)
        arr2 = fixNums(nums2)
        arr = []
        n1 = len(arr1)
        n2 = len(arr2)

        for i in range(n1):
            for j in range(n2):
                if arr1[i] == arr2[j]:
                    arr.append(arr1[i])

        return arr
