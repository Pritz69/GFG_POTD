#User function Template for python3

class Solution:
	def is_bleak(self, n):
		# Code here
        def countsetbits(x) :
            c =0 
            while x>0 :
                if x%2==1 :
                    c +=1
                x //=2
            return c
        for i in range(1,32) :
            if n-i and countsetbits(n-i)==i :
                return 0
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_bleak(n)
		print(ans)

# } Driver Code Ends