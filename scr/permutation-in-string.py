#url https://leetcode.com/problems/permutation-in-string
#writtenby:anhty9le	

def fixS(s):
    arr=[]
    n=len(s)
    for i in range(n):
        arr.append(s[i])
    return arr

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        n1=len(s1)
        n2=len(s2)
        arr1=fixS(s1)
        arr1.sort()
        arr2=fixS(s2)
        
        for i in range(n2-n1+1):
            arr=arr2[i:i+n1]
            arr.sort()
            if arr==arr1: return True
        return False
            
        