#User function Template for python3

#User function Template for python3
class Solution:

    def nthRowOfPascalTriangle(self,n):
        # code here
        if n==1 :
            return [1]
        if n==2 :
            return [1,1]
        l=[[1],[1,1]]
        for i in range(n-2) :
            nl=[1]
            pl=l[-1]
            for i in range(1,len(pl)) :
                nl.append((pl[i-1]+pl[i])%(1000000007))
            nl.append(1)
            l.append(nl)
        s=l[-1]
        return s




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
        print("~")
# } Driver Code Ends