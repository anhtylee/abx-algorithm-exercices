#url https://leetcode.com/problems/majority-element/
#writtenby:anhty9le	

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        arr=[1 for i in range(n)]
                
        for i in range(n-1):
            if nums[i]==nums[i+1]: arr[i+1]=arr[i]+1
        
        m=max(arr)
            
        for i in range(n):
            if m==arr[i]: return nums[i]
        