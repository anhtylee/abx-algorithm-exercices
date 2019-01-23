# url https://leetcode.com/problems/find-pivot-index/
# writtenby:anhty9le


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSum = sum(nums)
        n = len(nums)

        for i in range(n):
            if sum(nums[0:i]) == sum(nums[i + 1:n]):
                return i

        return -1
