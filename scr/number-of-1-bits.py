#url https://leetcode.com/problems/number-of-1-bits/
#writtenby:anhty9le	

def binary(n):
    arr=[]
    while n!=0:
        arr.append(n%2)
        n=n//2
    return arr

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0: return 0
        return sum(binary(n))