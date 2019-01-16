https://leetcode.com/problems/arranging-coins/
#writtenby:anhty9le	

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        i=1
        sum=0
        while sum<n:
            sum+=i
            count+=1
            i+=1
            
        if sum>n:  count-=1
        return count
            
        