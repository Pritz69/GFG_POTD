
#User function Template for python3

def binarySearch(arr,n,x):
        i=0;j=n-1
        while(i<=j):
            mid=(i+j)//2
            if arr[mid]==x:
                return True
            elif arr[mid]>x:
                j=mid-1
            else:
                i=mid+1
        return False

class Solution:            
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	n=len(mat)
    	m=len(mat[0])
    	for i in mat:
    	    if i[0]<=x<=i[-1] and binarySearch(i,m,x):
    	        return True
    	return False
    	    



#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.searchRowMatrix(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends