#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        ml=float('inf')
        for x in arr :
            if len(x) < ml :
                ml=len(x)
        l=[]
        for x in arr :
            if len(x)==ml :
                l.append(x)
        lcp=""
        #print(l)
        for x in l :
            for i in range(len(x)-1,-1,-1) :
                substr=x[:i+1]
                f=0
                for w in arr :
                   if w[:i+1]!=substr :
                       f=1
                       break
                if f==0 :
                    return substr
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends