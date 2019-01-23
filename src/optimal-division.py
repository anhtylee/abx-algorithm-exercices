# url https://leetcode.com/problems/optimal-division/
# writtenby:anhty9le


class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)

        if n == 1:
            return str(nums[0])

        if n == 2:
            return str(nums[0]) + "/" + str(nums[1])

        s = ""
        s += str(nums[0]) + "/("
        i = 1

        while i < n - 1:
            s += str(nums[i]) + "/"
            i += 1
        s += str(nums[n - 1]) + ")"

        return s
