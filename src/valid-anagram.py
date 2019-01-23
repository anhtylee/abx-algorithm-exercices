# url https://leetcode.com/problems/valid-anagram/
# writtenby:anhty9le


def fixString(string):
    n = len(string)
    arrS = []

    for i in range(n):
        arrS.append(string[i])

    arrS.sort()

    return arrS


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return fixString(s) == fixString(t)
