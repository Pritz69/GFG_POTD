#User function Template for python3

class Solution:    
    ##Complete this function
    # function to convert a given Gray equivalent n to Binary equivalent.
    def grayToBinary(self,n):
        ##Your code here
        if n<=1 :
            return n
        l=[]
        while n :
            l.append(n%2)
            n //=2
        l=l[::-1]
        a=[0]*len(l)
        a[0]=l[0]
        for i in range(1,len(l)) :
            a[i]=a[i-1]^l[i]
        ans=0
        m=1
        for i in range(len(a)-1,-1,-1) :
            ans += a[i]*m
            m *=2
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.grayToBinary(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends