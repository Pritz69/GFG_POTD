from collections import defaultdict
class Solution:
    def celebrity(self, mat):
        # code here
        d=defaultdict(list)
        for i in range(len(mat)) :
            for j in range(len(mat)) :
                if mat[i][j]==1 :
                    d[j].append(i)
        for i in range(len(mat)) :
            c0=0
            for j in range(len(mat)) :
                if mat[i][j]==0 :
                    c0 +=1
            if c0==len(mat) and len(d[i])==len(mat)-1 :
                return i
        return -1
#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends