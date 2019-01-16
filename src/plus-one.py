#url https://leetcode.com/problems/plus-one/
#writtenby:anhty9le	

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        n=len(digits)
        
        if digits[n-1]<9: 
            digits[n-1]+=1
            return digits
        
        i=n-1
        while i>0 and digits[i]==9:
            digits[i]=0
            i-=1
        
        if i==-1: digits.insert(0,1)
        else: digits[i]+=1
            
        if digits[0]==10:
            digits[0]=0
            digits.insert(0,1)
            
        return(digits)