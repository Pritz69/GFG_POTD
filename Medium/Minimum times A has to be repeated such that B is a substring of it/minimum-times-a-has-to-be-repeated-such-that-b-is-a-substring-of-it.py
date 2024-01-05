#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here 
        if A==B :
            return 1
        s=A
        c=1
        while len(s) <= len(B) :
            s = s + A
            c +=1
            if B in s :
                return c
        s = s + A
        c +=1
        if B in s :
            return c
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends