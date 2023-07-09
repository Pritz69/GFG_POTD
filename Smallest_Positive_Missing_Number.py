class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        for i in range(n) :
            while arr[i]>=1 and arr[i] <=n and arr[i] != arr[arr[i]-1] :
                t=arr[arr[i]-1]
                arr[arr[i]-1]=arr[i]
                arr[i]=t
        for i in range(n) :
            if arr[i]!=i+1 :
                return i+1
        return n+1
