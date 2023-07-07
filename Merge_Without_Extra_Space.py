class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        #code here
        i=n-1
        j=0
        while i>=0  and j < m :
            if arr1[i] <= arr2[j] :
                break
            else :
                t=arr1[i]
                arr1[i]=arr2[j]
                arr2[j]=t
                i -=1
                j +=1
        arr1.sort()
        arr2.sort()
