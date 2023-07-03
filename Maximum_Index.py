#User function Template for python3
class Solution:

    def maxIndexDiff(self,arr,n):
        #code here
           lMin=[arr[0]]*n
           rMax=[arr[n-1]]*n
           
           for i in range(1, n):
               lMin[i]=min(arr[i], lMin[i-1])
           
           for i in range(n-2, -1, -1):
               rMax[i]=max(arr[i], rMax[i+1])
           
           i, j, ans=0, 0, -1
           while i<n and j<n:
               if lMin[i]<=rMax[j]:
                   ans=max(j-i, ans)
                   j+=1
               else:
                   i+=1
           return ans
