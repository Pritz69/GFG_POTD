#User function Template for python3

class Solution:
    def search(self, pattern, text):
        # code here
        l=len(pattern)
        ans=[]
        for i in range(len(text)) :
            if text[i:i+l]==pattern :
                ans.append(i+1)
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends