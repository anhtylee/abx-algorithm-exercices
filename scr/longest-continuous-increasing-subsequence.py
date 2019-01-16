#url https://leetcode.com/problems/longest-continuous-increasing-subsequence/
#writtenby:anhty9le	

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]: return 0
        n=len(nums)
        arrIndex=[1 for i in range(n)]
        for i in range(1,n):
            if nums[i-1]<nums[i]: arrIndex[i]=arrIndex[i-1]+1
        return max(arrIndex)
        
        