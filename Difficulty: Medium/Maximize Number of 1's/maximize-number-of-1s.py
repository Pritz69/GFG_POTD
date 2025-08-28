class Solution:
    def maxOnes(self, arr, k):
        # code here
        i =0
        maxlen =0
        for j in range(len(arr)):
            if arr[j]==0:
                k-=1
            if k<0:
                if arr[i]==0:
                    k+=1
                i+=1
            if k >=0:
                maxlen = max(maxlen,j-i+1)
        return maxlen