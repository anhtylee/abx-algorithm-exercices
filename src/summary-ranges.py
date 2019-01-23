# url https://leetcode.com/problems/summary-ranges/
# writtenby:anhty9le


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums.append(0)
        n = len(nums)
        i = 0
        arr = []

        while i < n - 1:
            k = 0

            while nums[i + k] + 1 == nums[i + k + 1] and i + k < n - 2:
                k += 1

            if k != 0:
                arr.append(str(nums[i]) + "->" + str(nums[i + k]))
            else:
                arr.append(str(nums[i]))

            i += k + 1

        return arr
