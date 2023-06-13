class Solution:
    def kLargest(self,arr, n, k):
        # code here
        l=[0]*k
        count=0
        arr.sort()
        for i in range(len(arr)-1,-1,-1):
            if count<k:
                l[count]=arr[i]
                count=count+1
            else:
                break
        return l  
