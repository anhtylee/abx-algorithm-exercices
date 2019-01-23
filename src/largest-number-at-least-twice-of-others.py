# url https://leetcode.com/problems/largest-number-at-least-twice-of-others/
# writtenby:anhty9le


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numMax = max(nums)
        n = len(nums)

        for i in range(n):
            if numMax == nums[i]:
                pos = i
            elif nums[i] != 0:
                if numMax < nums[i] * 2:
                    return -1

        return pos
