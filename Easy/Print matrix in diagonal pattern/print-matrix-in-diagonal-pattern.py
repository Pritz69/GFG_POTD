# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        from collections import defaultdict
        
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                d[i+j].append(mat[i][j])
                
        ans = []
        for k in sorted(d):
            if k&1:
                ans.extend(d[k])
            else:
                ans.extend(d[k][::-1])
        return ans

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends