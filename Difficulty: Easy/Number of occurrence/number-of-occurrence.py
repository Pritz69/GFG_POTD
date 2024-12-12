class Solution:
    def countFreq(self, arr, target):
        #code here
        lb=-1
        for i,x in enumerate(arr) :
            if x==target :
                lb=i
                break
        ub=-1
        for i in range(len(arr)-1,-1,-1) :
            if arr[i]==target :
                ub=i
                break
        #print(ub,lb)
        if not (ub==-1 and lb==-1) :
            return (ub-lb)+1
        return 0
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends