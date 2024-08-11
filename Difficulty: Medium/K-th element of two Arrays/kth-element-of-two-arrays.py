#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        
        n=len(arr1)
        m=len(arr2)
        if m < n :
            return self.kthElement(k,arr2,arr1)
        
        left=k
        low=max(0,k-m)
        high=min(k,n)
        while low <= high :
            mid1=(low+high)>>1
            mid2=left-mid1
            l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < n else float('inf')
            r2 = arr2[mid2] if mid2 < m else float('inf')
            if l1 <= r2 and l2 <= r1 :
                return max(l1,l2)
            elif l1 > r2 :
                high=mid1-1
            else :
                low=mid1+1
        return 0


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
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends