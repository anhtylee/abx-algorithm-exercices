#url https://leetcode.com/problems/convert-a-number-to-hexadecimal/
#writtenby:anhty9le

def binary(num):
    arr=[]
    
    while num!=0:
        arr.append(num%2)
        num=num//2
    return arr

def hexde(num):
    arr=""
    
    while num!=0:
        r=num%16
        if r==10: arr+="a"
        elif r==11: arr+="b"
        elif r==12: arr+="c"
        elif r==13: arr+="d"
        elif r==14: arr+="e"
        elif r==15: arr+="f"
        else: arr+=str(r)
        num=num//16
    return arr[::-1]

        

    
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: return "0"
        if num>0: return(hexde(num))
    
        arr=binary(abs(num))
        while len(arr)<32:
            arr.append(0)
         
        n=len(arr)
        
        for i in range(n):
            if arr[i]==1:
                for j in range(i+1,n):
                    arr[j]=1-arr[j]
                break
        sum=0
        for i in range(n):
            sum+=arr[i]*math.pow(2,i)
        
        return hexde(int(sum))
