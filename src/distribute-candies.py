# url https://leetcode.com/problems/distribute-candies/
# writtenby:anhty9le


class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        n = len(candies)
        k = 0
        candies.sort()

        for i in range(n):
            if candies[i] == candies[i - 1]:
                k += 1
                candies[i - 1] = -1

        if n - k < n / 2:
            return n - k
        else:
            return n / 2
