#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        c=0
        n=1
        i=0
        while i < len(arr) :
            while n != arr[i] :
                c +=1
                if c==k :
                    return n
                n +=1
            i+=1
            n+=1
        n -=1
        while c != k :
            n +=1
            c +=1
        return n

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.kthMissing(A, D)
        print(ans)
        print("~")

# } Driver Code Ends