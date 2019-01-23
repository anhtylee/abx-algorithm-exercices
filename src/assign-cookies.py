# url https://leetcode.com/problems/assign-cookies/
# writtenby:anhty9le


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        count = 0
        nchild = len(g)
        ncake = len(s)
        g.sort()
        s.sort()
        for i in range(nchild):
            for j in range(ncake):
                if g[i] <= s[j]:
                    count += 1
                    s[j] = 0
                    break
        return count
