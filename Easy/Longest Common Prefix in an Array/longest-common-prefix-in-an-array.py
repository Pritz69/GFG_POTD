#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        m=len(arr[0])
        word=""
        for x in arr :
            if len(x) <= m :
                m=len(x)
                word=x
        #print(word,m)
        for i in range(m,0,-1) :
            f=0
            for x in arr:
                if word[0:i] == x[0:i] :
                    continue
                else :
                    f=1
                    break
            if f==0 :
                break
        if f==1 :
            return -1
        return word[0:i]
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends