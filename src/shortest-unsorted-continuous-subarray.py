#url https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
#writtenby:anhty9le	

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n==1: return 0
        arr=nums.copy()
        arr.sort()
        left=0
        right=n-1
        while arr[left]==nums[left] and left<n-1: left+=1
        while arr[right]==nums[right] and right>0: right-=1
        
        if right<left: return 0
        return right-left+1