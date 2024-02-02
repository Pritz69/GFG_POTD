#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        st=['-','1','2','3','4','5','6','7','8','9','0']
        st=set(st)
        for i in range(len(s)) :
            if s[i]=='-' and i >0 :
                return -1
            if s[i] not in st :
                return -1
        f=0
        if s[0]=='-' :
            f=1
            s=s[1:]
        ans=0
        for x in s :
            d=ord(x)-48
            ans=ans*10 +d
        if f==1 :
            return ans*-1
        else :
            return ans
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends