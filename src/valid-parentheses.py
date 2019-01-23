# url https://leetcode.com/problems/valid-parentheses/
# writtenby:anhty9le


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        """

        r = True

        while r is True and s != "":
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")

            if s.find("()") < 0 and s.find("{}") < 0 and s.find("[]") < 0:
                r = False

        return s == ""
