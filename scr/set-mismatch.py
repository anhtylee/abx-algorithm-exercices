#url https://leetcode.com/problems/set-mismatch/
#writtenby:anhty9le	

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.append(0)
        nums.append(max(nums)+2)
        nums.sort()
        print(nums)
        n=len(nums)
        arr=[]
        
        for i in range(0,n-1):
            if nums[i]==nums[i+1]:
                arr.append(nums[i])
                break
        for i in range(0,n-1):
            if nums[i]+1<nums[i+1]:
                arr.append(nums[i]+1)
                break
        return arr
        