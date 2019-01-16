#url https://leetcode.com/problems/base-7/
#writtenby:anhty9le

def base7(num):
    s=""
    while num!=0:
        s+=str(num%7)
        num=num//7
    return s[::-1]

        
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: return "0"
        sign=True
        if num<0:
            sign=False
            num=abs(num)
        s=base7(num)
        if sign==False: s="-"+s
        return s
        

