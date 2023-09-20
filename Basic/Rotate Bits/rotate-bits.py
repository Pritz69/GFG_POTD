#User function Template for python3

class Solution:
    def rotate(self, N, D):
        # code here
        while (D>16):
            D= D%16
        right_rotation = (N>>D) | (N<<(16-D)) & 0xFFFF
        left_rotation = (N<<D | N>>(16-D))& 0xFFFF

        return [left_rotation,right_rotation]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends