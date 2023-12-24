

from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        # code here
        l=[]
        for i in range(n) :
            l.append((price[i],i+1))
        l.sort()
        c=0
        s=0
        #print(l)
        for i in l :
            a,v=i[0],i[1]
            p=0
            if s+(a*v)<=k :
                s += (a*v)
                c += v
                #print(s,c)
            else :
                r=k-s
                c += r//a
                #print(r,c)
                break
                #for j in range(1,v+1):
                #    if s+(a*j) <= k :
                #        p=j
                #    else :
                #        break
                #s += (a*p)
                #c += p
        return c



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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends