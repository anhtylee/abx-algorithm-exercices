#url https://leetcode.com/problems/valid-mountain-array/
#writtenby:anhty9le	

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        n=len(A)
        if n<3: return False
        count=0
        i=0
        
        while i<n-1 and A[i]<A[i+1]:
            i+=1
            
        if i+1==n or i==0: return False
        
        while i<n-1 and A[i]>A[i+1]:
            i+=1
            
        return i+1==n
            
            
