from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        l=[]
        for i in range(N) :
            l.append((S[i],F[i],i+1))
        l.sort(key=lambda x :x[1])
        #print(l)
        ans=[]
        lt=0
        for i in range(N) :
            st=l[i][0]
            if st > lt :
                ans.append(l[i][2])
                lt=l[i][1]
        #print(ans)
        return sorted(ans)
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends