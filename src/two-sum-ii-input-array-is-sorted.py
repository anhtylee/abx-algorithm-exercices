#url https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#writtenby:anhty9le	

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(numbers)
        k=1
        for i in range(n):
            for j in range(i+1,n):
                if numbers[i]==numbers[i+1] and numbers[i]*2<target:
                    numbers.pop(i)
                    n-=1
                    k+=1
                if numbers[i]+numbers[j]>target: break
                if numbers[i]+numbers[j]==target:
                    return(i+k,j+k)
                