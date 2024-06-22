class Solution:
    def ExtractNumber(self,sentence):
        #code here
        l=[]
        for x in sentence.split(" "):
            if '9' not in x and len(x) >= 1 and ord(x[0]) >=48 and ord(x[0]) <= 57 :
                l.append(int(x))
        if not l :
            return -1
        return sorted(l)[-1]

#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends