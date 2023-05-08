#User function Template for python3

class Solution():
    def modulo(self, s, m):
        #your code goes here
        k=int(s,2)
        return k%m


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s,m = input().split()
        m = int(m)
        print(Solution().modulo(s, m))

# } Driver Code Ends
