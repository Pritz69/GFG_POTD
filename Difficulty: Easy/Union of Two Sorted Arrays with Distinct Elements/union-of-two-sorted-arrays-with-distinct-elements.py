#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        ans=[]
        i=0
        j=0
        n=len(a)
        m=len(b)
        while i < n and j<m :
            if a[i]==b[j] :
                ans.append(a[i])
                i +=1
                j +=1
            elif a[i]<b[j] :
                ans.append(a[i])
                i+=1
            else :
                ans.append(b[j])
                j+=1
        while i < n :
            ans.append(a[i])
            i+=1
        while j < m :
            ans.append(b[j])
            j+=1
        return ans

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")
# } Driver Code Ends