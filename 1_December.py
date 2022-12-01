    def rearrange(self,arr, n): 
        ##Your code here
        l,r=0,n-1
        lit=[]
        while l<=r :
            lit.append(arr[r])
            lit.append(arr[l])
            l +=1
            r -=1
        for i in range(n):
            arr[i]=lit[i]
