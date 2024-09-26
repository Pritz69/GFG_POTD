#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        p=arr[0]
        c=0
        m=float('-inf')
        for i in range(1,len(arr)) :
            if arr[i] > p :
                c=c+1
            else :
                m=max(m,c)
                c=0
            p=arr[i]
        m=max(m,c)
        return m
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends