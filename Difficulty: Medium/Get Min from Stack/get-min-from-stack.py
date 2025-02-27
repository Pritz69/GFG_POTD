class Solution:

    def __init__(self):
        # code here
        self.st = []
        self.min_st = []
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        self.st.append(x)
        if not self.min_st or x<=self.min_st[-1]:
            self.min_st.append(x)

    # Remove the top element from the Stack
    def pop(self):
        # code here
        if not self.st:
            return
        val = self.st.pop()
        if val == self.min_st[-1]:
            self.min_st.pop()
        

    # Returns top element of Stack
    def peek(self):
        # code here
        if self.st:
            return self.st[-1]
        else:
            return -1

    # Finds minimum element of Stack
    def getMin(self):
        # code here
        if not self.min_st:
            return -1
        else:
            return self.min_st[-1]



#{ 
 # Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        q = int(input())  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input().split()))

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends