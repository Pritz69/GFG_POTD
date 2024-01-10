#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		#Complete the function
		s=0
		m=0
		d={}
		for i in range(n) :
		    s +=arr[i]
		    if s%K==0 :
		        m=max(m,i+1)
		    if s%K in d :
		        m=max(m,i-d[s%K])
            else :
                d[s%K]=i
        return m



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends