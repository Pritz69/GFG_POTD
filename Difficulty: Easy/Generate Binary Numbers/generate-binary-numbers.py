class Solution:
    def generateBinary(self, n):
        # code here
        def f(x) :
            s=""
            while x :
                s=str(x%2)+s
                x=x//2
            return s
        ans=[]
        for i in range(1,n+1) :
            ans.append(f(i))
        return ans