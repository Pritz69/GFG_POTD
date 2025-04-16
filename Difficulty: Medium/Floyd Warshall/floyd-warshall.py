#User function template for Python

class Solution:
	def floydWarshall(self, dist):
		#Code here
        n = len(dist)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < 1e8 and dist[k][j] < 1e8:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.floydWarshall(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end=" ")
            print()
        print("~")

# } Driver Code Ends