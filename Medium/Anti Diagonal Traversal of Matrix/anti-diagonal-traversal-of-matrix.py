#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,matrix):
        # Code here
        l=[]
        for j in range(len(matrix)) :
            i=0
            while i < len(matrix) and j<len(matrix) and j>=0:
                l.append(matrix[i][j])
                i +=1
                j -=1
        for i in range(1,len(matrix)) :
            j=len(matrix)-1
            while i < len(matrix) and j >=0 :
                l.append(matrix[i][j])
                i +=1
                j -=1
        return l
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends