#url https://leetcode.com/problems/intersection-of-two-arrays-ii/
#writtenby:anhty9le	

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        n1=len(nums1)
        n2=len(nums2)
        arr=[]
        
        for i in range(n1):
            for j in range(n2):
                if nums1[i]==nums2[j]:
                    arr.append(nums1[i])
                    nums1[i]="b"
                    nums2[j]="a"
        return arr