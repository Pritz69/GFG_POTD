#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    cs=0
    mas=float('-inf')
    for x in arr :
        cs += x
        mas=max(mas,cs)
        if cs <0 :
            cs=0
    cs=0
    mis=float('inf')
    for x in arr :
        cs += x
        mis=min(mis,cs)
        if cs > 0 :
            cs=0
    diff=sum(arr)-mis
    return max(mas,diff)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends