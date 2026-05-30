class Solution:
    def replaceElements(self, arr):
        # code here
        ans=[arr[0]^arr[1]]
        for i in range(1,len(arr)-1) :
            ans.append(arr[i-1]^arr[i+1])
        ans.append(arr[len(arr)-2]^arr[len(arr)-1])
        for i in range(len(ans)) :
            arr[i]=ans[i]
        return arr