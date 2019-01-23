# url https://leetcode.com/problems/island-perimeter/
# writtenby:anhty9le


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        maps = [[0 for row in range(0, c + 2)] for col in range(0, r + 2)]

        for i in range(r):
            for j in range(c):
                maps[i + 1][j + 1] = grid[i][j]
        cv = 0

        for i in range(1, r + 1):
            for j in range(1, c + 1):
                cv += maps[i][j] * ((1 - maps[i][j + 1]) + (1 - maps[i]
                                                            [j - 1]) + (1 - maps[i + 1][j]) + (1 - maps[i - 1][j]))

        return cv
