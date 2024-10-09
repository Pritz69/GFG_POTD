#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        row = col = len(mat)
        linked_list_matrix = [[None for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                linked_list_matrix[i][j] = Node(mat[i][j])
        for i in range(row):
            for j in range(col):
                curr = linked_list_matrix[i][j]
                if j + 1 < col:  
                    curr.right = linked_list_matrix[i][j + 1]
                if i + 1 < row: 
                    curr.down = linked_list_matrix[i + 1][j]
        return  linked_list_matrix[0][0]
                

#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()

# } Driver Code Ends