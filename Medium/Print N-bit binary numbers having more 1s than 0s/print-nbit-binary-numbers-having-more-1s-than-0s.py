#User function Template for python3
class Solution:
    def find(self,n,ans,temp,zero,one):
        if len(temp)==n:
            ans.append(temp)
            return
        self.find(n,ans,temp+'1',zero,one+1)
        if zero<one:
            self.find(n,ans,temp+'0',zero+1,one)
        
    def NBitBinary(self, n):
        ans=[]
        temp=''
        self.find(n,ans,temp,0,0)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends