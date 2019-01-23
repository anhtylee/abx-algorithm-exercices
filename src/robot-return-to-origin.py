# url https://leetcode.com/problems/robot-return-to-origin/
# writtenby:anhty9le


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        n = len(moves)
        i = j = 0

        for k in range(n):
            if moves[k] == "U":
                j += 1
            elif moves[k] == "D":
                j -= 1
            elif moves[k] == "R":
                i += 1
            elif moves[k] == "L":
                i -= 1

        return i == 0 and j == 0
