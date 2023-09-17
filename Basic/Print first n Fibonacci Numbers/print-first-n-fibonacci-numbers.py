#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        if n==1 :
            return [1]
        if n==2 :
            return [1,1]
        a=1
        b=1
        c=0
        l=[1,1]
        for i in range(n-2) :
            c=a+b
            l.append(c)
            a=b
            b=c
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends