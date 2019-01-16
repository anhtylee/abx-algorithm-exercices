#url https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#writtenby:anhty9le	

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        n=len(nums)
        while i<n-1:
            if nums[i]==nums[i+1]:
                nums.pop(i)
                i-=1
                n-=1
            i+=1
        return n
        