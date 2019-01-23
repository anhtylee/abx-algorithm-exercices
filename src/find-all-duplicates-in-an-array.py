# url https://leetcode.com/problems/find-all-duplicates-in-an-array/
# writtenby:anhty9le


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        i = 0
        arr = []

        while i < n - 1:
            if nums[i] == nums[i + 1]:
                arr.append(nums[i])
                i += 1
            i += 1

        return arr
