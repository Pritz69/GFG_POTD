#User function Template for python3


class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    

    def rotateby90(self, mat): 
        def reverse(arr):
            l,h=0,len(arr)-1
            while l<h:
                arr[l],arr[h]=arr[h],arr[l]
                l+=1
                h-=1
        for row in mat:
            reverse(row)
        rows,cols=len(mat),len(mat[0])
        for i in range(rows):
            for j in range(i+1,cols):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
                
              
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        n = int(data[index])
        index += 1
        matrix = []
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.rotateby90(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()

        print("~")

# } Driver Code Ends