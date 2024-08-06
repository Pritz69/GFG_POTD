#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        c=0
        for x in str.split(".") :
            if 0 <= int(x) <= 255 :
                c +=1
                continue
            else :
                return False
        return c==4


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends