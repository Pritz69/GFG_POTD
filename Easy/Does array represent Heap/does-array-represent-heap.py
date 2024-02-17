class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here            
        l=0
        for i in range(n) :
            if (i+l+1 <n and arr[i] < arr[i+l+1] ) or (i+l+2<n and arr[i] < arr[i+l+2]) :
                return 0
            l +=1
        return 1

#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends