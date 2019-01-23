# url https://leetcode.com/problems/array-partition-i/
# writtenby:anhty9le


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort(reverse=True)
        n = len(nums) / 2
        for i in range(n):
            sum += nums[2 * i + 1]
        return sum
