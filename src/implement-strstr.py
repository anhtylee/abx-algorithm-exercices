# url https://leetcode.com/problems/implement-strstr/
# writtenby:anhty9le


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
