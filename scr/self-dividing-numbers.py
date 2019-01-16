#url https://leetcode.com/problems/self-dividing-numbers/
#writtenby:anhty9le	

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        arr=[]
        for num in range(left,right+1):
            n=num
            check=True
            while n!=0:
                i=n%10
                if i==0: check=False
                elif num%i!=0: check=False
                n=n//10
            if check==True: arr.append(num)
        return arr
                