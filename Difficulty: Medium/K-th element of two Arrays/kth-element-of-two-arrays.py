#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        i,j=0,0
        n=len(a)
        m=len(b)
        ans=[]
        while i<n and j<m :
            if a[i] <= b[j] :
                ans.append(a[i])
                i +=1
            else :
                ans.append(b[j])
                j +=1
        while i <n :
            ans.append(a[i])
            i +=1
        while j < m :
            ans.append(b[j])
            j +=1
        return ans[k-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, k))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends