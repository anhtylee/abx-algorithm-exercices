# url https://leetcode.com/problems/relative-ranks/
# writtenby:anhty9le


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        n = len(nums)
        numssort = []

        for i in range(n):
            numssort.append(nums[i])

        numssort.sort(reverse=True)
        ranks = [0 for i in range(n)]

        for i in range(n):
            for j in range(n):
                if numssort[i] == nums[j]:
                    ranks[j] = i + 1

        for i in range(n):
            if ranks[i] == 1:
                ranks[i] = "Gold Medal"
            elif ranks[i] == 2:
                ranks[i] = "Silver Medal"
            elif ranks[i] == 3:
                ranks[i] = "Bronze Medal"
            else:
                ranks[i] = str(ranks[i])

        return ranks
