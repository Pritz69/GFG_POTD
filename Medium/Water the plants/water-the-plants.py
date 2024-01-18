#User function Template for python3

class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        l=[0]*(n)
        for i,x in enumerate(gallery) :
            if x!=-1 :
                le=max(0,i-x)
                ri=i+x
                l[le]=max(l[le],ri)
        #print(l)
        c=0
        le,r=0,0
        while r < n :
            f=0
            for i in range(le,r+1) :
                f=max(f,l[i])
            le=r+1
            r=f+1
            if le>r :
                return -1
            c +=1
        return c
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        gallery = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.min_sprinklers(gallery,n))

# } Driver Code Ends