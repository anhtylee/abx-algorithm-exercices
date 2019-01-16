#url https://leetcode.com/problems/find-smallest-letter-greater-than-target/
#writtenby:anhty9le	

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n=len(letters)
        for i in range(n):
            if ord(letters[i])> ord(target): return letters[i]
        return letters[0]