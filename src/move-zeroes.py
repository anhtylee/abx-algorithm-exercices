#url https://leetcode.com/problems/move-zeroes/
#writtenby:anhty9le	

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        count=0
        while i<n:
            if nums[i]==0:
                nums.pop(i)
                i-=1
                n-=1
                count+=1
            i+=1
        for i in range(count):
            nums.append(0)