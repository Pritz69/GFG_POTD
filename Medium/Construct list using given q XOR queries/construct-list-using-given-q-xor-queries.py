
from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        # code here
        l=[]
        x=0
        for i in range(q-1,-1,-1) :
            if queries[i][0]==0 :
                l.append(queries[i][1]^x)
            else :
                x=x^queries[i][1]
        l.append(0^x)
        return sorted(l)


#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        q = int(input())

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.constructList(q, queries)

        IntArray().Print(res)

# } Driver Code Ends