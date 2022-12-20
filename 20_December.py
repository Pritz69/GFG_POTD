class Solution:
    def maxDistance (self, arr, n) : 
        #Complete the function
        max1, min1, max2, min2=arr[0],arr[0],arr[0],arr[0]
        for i in range(1, n):
            max1=max(max1, arr[i]-i)
            min1=min(min1, arr[i]-i)
            max2=max(max2, arr[i]+i)
            min2=min(min2, arr[i]+i)
        return max(max1-min1, max2-min2)
