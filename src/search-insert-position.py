# url https://leetcode.com/problems/search-insert-position/
# writtenby:anhty9le


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        if target > nums[n - 1]:
            return n

        if target == nums[n - 1]:
            return n - 1

        for i in range(n):
            if target < nums[i]:
                if target == nums[i - 1]:
                    return i - 1
                else:
                    return i
