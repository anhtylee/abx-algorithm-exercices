#url https://leetcode.com/problems/reshape-the-matrix/
#writtenby:anhty9le	

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        r1=len(nums)
        c1=len(nums[0])
        if r1*c1!=r*c: return nums
        else:
            arrTemp=[]
            arrResult=[]
            arrResult.append([])
            
            for i in range(r1):
                for j in range(c1):
                    arrTemp.append(nums[i][j])
           
                    
            arrResult=[[0 for row in range(0,c)] for col in range(0,r)] 
                           
            k=0
            for i in range(r):
                for j in range(c):
                    arrResult[i][j]=arrTemp[k]
                    k+=1
        
        return arrResult