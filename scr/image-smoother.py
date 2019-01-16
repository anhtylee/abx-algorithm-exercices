#url https://leetcode.com/problems/image-smoother/
#writtenby:anhty9le	

def avg(nums,posI,posJ):
    count=0
    sum=0
    m=len(nums)
    n=len(nums[0])
    for i in range(-1,2):
        for j in range(-1,2):
            if posI+i>=0 and posI+i<m and posJ+j>=0 and posJ+j<n:
               sum+=nums[posI+i][posJ+j]
               count+=1
    return sum/count
                
    

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(M)
        n=len(M[0])
        Result=[[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                Result[i][j]=((avg(M,i,j)))
                
        return Result
            
     