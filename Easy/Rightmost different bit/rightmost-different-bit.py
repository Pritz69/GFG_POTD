#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




    
# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find the first position with different bits.
    def posOfRightMostDiffBit(self,m,n):
        #Your code here
        if m==n :
            return -1
        ans=m^n
        c=0
        f=0
        while f != 1:
            if ans & (1<<c) :
               f=1
               break
            c +=1
        return c+1
        
        #position = 1
        #while xor:
        #    if xor & 1:
        #        return position
        #    else:
        #       xor = xor >> 1
        ##       position += 1
      

#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        ob=Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends