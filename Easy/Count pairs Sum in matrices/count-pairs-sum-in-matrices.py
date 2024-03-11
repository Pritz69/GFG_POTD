#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		# code here
		d={}
        for i in range(n) :
            for j in range(n) :
                v=mat2[i][j]
                d[v]=d.get(v,0)+1
        c=0
        for i in range(n) :
            for j in range(n) :
                v=mat1[i][j]
                if x-v in d :
                    c += d[x-v]
        return c
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends