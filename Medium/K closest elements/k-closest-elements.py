#User function Template for python3

class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        for i in range(n) :
            arr[i]=(arr[i],abs(arr[i]-x))
        arr.sort(key=lambda elem: (elem[1], -elem[0]))
        ans=[]
        i=0
        while len(ans) != k  :
            if arr[i][1]==0 :
                i +=1
                continue
            ans.append(arr[i][0])
            i +=1
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends