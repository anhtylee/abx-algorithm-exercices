# url https://leetcode.com/problems/ransom-note/
# writtenby:anhty9le


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for i in range(len(ransomNote)):
            if magazine.find(ransomNote[i]) == -1:
                return False

            magazine = magazine.replace(ransomNote[i], "-", 1)

        return True
