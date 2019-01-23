# url https://leetcode.com/problems/max-consecutive-ones/
# writtenby:anhty9le


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        Result = 0
        k = 0
        check = 1
        n = len(nums)

        for i in range(n):
            k += nums[i]
            check *= nums[i]
            if check == 0:
                if Result < k:
                    Result = k
                k = 0
                check = 1

        return Result
