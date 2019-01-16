#url https://leetcode.com/problems/minimum-index-sum-of-two-lists/
#writtenby:anhty9le	

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        n1=len(list1)
        n2=len(list2)
        pos=n1+n2
        arrR=[]
        for i in range(n1):
            for j in range(n2):
                if list1[i]==list2[j]:
                    if pos>i+j:
                        pos=i+j
                        
        for i in range(n1):
            for j in range(n2):
                if list1[i]==list2[j]:
                    if pos==i+j:
                        arrR.append(list1[i])
        return arrR
        