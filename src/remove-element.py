# url https://leetcode.com/problems/remove-element/
# writtenby:anhty9le


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        i = 0

        while i < n:
            if val == nums[i]:
                nums.pop(i)
                n -= 1
                i -= 1
            i += 1

        return n
