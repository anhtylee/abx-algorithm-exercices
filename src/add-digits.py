#url https://leetcode.com/problems/add-digits/
#writtenby:anhty9le	

class Solution(object):
    def addDigits(self,num):
        if num<10: return num
        else: return self.addDigits(num%10+self.addDigits((num//10)))
