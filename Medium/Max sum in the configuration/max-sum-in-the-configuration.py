#User function Template for python3

def max_sum(l,n):
    #code here
    m=float('-inf')
    cmsm=sum(l)
    v=0
    for i in range(n) :
        v += i*l[i]
    m=max(m,v)
    for i in range(1,n) :
        nv= v - (cmsm-l[i-1]) + (l[i-1]*(n-1))
        v=nv
        m=max(m,nv)
    return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends