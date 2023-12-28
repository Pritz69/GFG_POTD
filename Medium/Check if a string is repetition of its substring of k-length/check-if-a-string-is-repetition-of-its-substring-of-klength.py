#User function Template for python3
class Solution:
	def kSubstrConcat(self, n, s, k):
		# Your Code Here
        if n%k !=0 :
            return 0
        if n==k :
            return 1
        d={}
        i=0
        while i <= n-k :
            a=s[i:i+k]
            d[a]=d.get(a,0)+1
            i +=k
        if len(d) > 2 :
            return 0
        c=0
        #print(d)
        for x in d :
            if d[x] >= 2 :
                c +=1
        if c==2 :
            return 0
        else :
            return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends