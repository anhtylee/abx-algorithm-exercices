# url https://leetcode.com/problems/student-attendance-record-i/
# writtenby:anhty9le


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count("A") > 1:
            return False

        if s.count("LLL") > 0:
            return False

        return True
