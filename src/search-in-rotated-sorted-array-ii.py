#url https://leetcode.com/problems/search-in-rotated-sorted-array-ii
#writtenby:anhty9le	

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n=len(nums)
        if n==0: return False
        if target>=nums[0]:
            for i in range(n):
                if target==nums[i]: return True
        else: 
            for i in range(n):
                if target==nums[n-i-1]: return True
        return False
            
        