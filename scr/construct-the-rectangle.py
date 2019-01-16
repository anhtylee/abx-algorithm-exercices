#url https://leetcode.com/problems/construct-the-rectangle/
#writtenby:anhty9le

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
        L=int(round(math.sqrt(area)))
        i=L
        while area%i!=0:
            i+=1
        a=i
        b=area//i
        if a>b: return (a,b)
        else: return (b,a)
            
            