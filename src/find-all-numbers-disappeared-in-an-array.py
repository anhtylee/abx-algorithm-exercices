#url https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
#writtenby:anhty9le	

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Result=[]
        nums.append(0)
        nums.sort()
        n=len(nums)
        nums.append(n)
               
        for i in range(n):
            low=nums[i]
            high=nums[i+1]
            while low+1<high: 
                Result.append(low+1)
                low+=1
        return Result