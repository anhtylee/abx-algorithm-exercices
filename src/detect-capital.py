#url https://leetcode.com/problems/detect-capital/
#writtenby:anhty9le

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or (word[0].isupper and word[1:].islower())