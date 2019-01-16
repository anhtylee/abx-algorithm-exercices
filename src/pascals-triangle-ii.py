#url https://leetcode.com/problems/pascals-triangle-ii/
#writtenby:anhty9le	

class Solution(object):
    def getRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        n=numRows+2
        arr=[[0 for i in range(n)]for j in range(n)]
        arr[0][0]=1
        i=1
        
        while i<n:
            for j in range(i):
                arr[i][j]=(arr[i-1][j-1]+arr[i-1][j])
            i+=1
       
        Result=[]
        
        for i in range(n-1):
            Result.append(arr[n-1][i])
        return(Result)
            