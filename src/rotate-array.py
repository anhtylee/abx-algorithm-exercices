# url https://leetcode.com/problems/rotate-array/
# writtenby:anhty9le


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        if n < k:
            k = k % n

        arr = []
        arr = nums[:n - k]

        for i in range(n - k):
            nums.pop(0)

        for i in range(n - k):
            nums.append(arr[i])
