#url https://leetcode.com/problems/keyboard-row/
#writtenby:anhty9le	

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s=["","",""]
        s[0]="qwertyuiopQWERTYUIOP"
        s[1]="asdfghjklASDFGHJKL"
        s[2]="zxcvbnmZXCVBNM"
        n=len(words)
        arr=[]
        
        for i in range(n):
            check=True
            for k in range(3):
                if s[k].find(words[i][0])>-1:
                    for j in range(len(words[i])):
                        if s[k].find(words[i][j])<0: check=False
            if check: arr.append(words[i])
        return arr
        
        
                
        