#User function Template for python3

class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        s,m=0,float('-inf')
        l,r=0,0
        st=0
        while r < n :
            s += a[r]
            if r-l +1 == k :
                m=max(m,s)
            if r-l +1 > k :
                m=max(m,s)
                st += a[l]
                l +=1
                if st < 0 :
                    s -=st
                    st =0
                m=max(m,s)
            r +=1
        return m
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends