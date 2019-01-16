#url https://leetcode.com/problems/reverse-words-in-a-string-iii/
#writtenby:anhty9le	

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s+=" "
        n=len(s)
        clone=""
        txt=""
        for i in range(n):
            if s[i]==" ": 
                txt+=clone[::-1]+" "
                clone=""
            else: clone+=s[i]
            
            
        return txt.rstrip()
        