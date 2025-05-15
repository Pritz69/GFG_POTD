class Solution:
	def countSubstring(self, s):
		# code here
		d={}
        count=0
        for i in s:
            if i in d:
                count+=d[i]
            d[i]=d.get(i,0)+1
        return count+len(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends