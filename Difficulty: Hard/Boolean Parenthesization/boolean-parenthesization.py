#User function Template for python3
class Solution:
    def evaluate(self, b1, b2, op):
        if op == '&':
            return (b1 & b2) == 1
        if op == '|':
            return (b1 | b2) == 1
        return (b1 ^ b2) == 1

    def countWays(self, s):
        n = len(s)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        for i in range(0, n, 2):
            dp[i][i][1] = 1 if s[i] == 'T' else 0
            dp[i][i][0] = 1 if s[i] == 'F' else 0

        for length in range(2, n, 2):
            for i in range(0, n - length, 2):
                j = i + length
                dp[i][j][0] = dp[i][j][1] = 0

                for k in range(i + 1, j, 2):
                    op = s[k]
                    leftTrue = dp[i][k - 1][1]
                    leftFalse = dp[i][k - 1][0]
                    rightTrue = dp[k + 1][j][1]
                    rightFalse = dp[k + 1][j][0]

                    if self.evaluate(1, 1, op):
                        dp[i][j][1] += leftTrue * rightTrue
                    if self.evaluate(1, 0, op):
                        dp[i][j][1] += leftTrue * rightFalse
                    if self.evaluate(0, 1, op):
                        dp[i][j][1] += leftFalse * rightTrue
                    if self.evaluate(0, 0, op):
                        dp[i][j][1] += leftFalse * rightFalse

                    if not self.evaluate(1, 1, op):
                        dp[i][j][0] += leftTrue * rightTrue
                    if not self.evaluate(1, 0, op):
                        dp[i][j][0] += leftTrue * rightFalse
                    if not self.evaluate(0, 1, op):
                        dp[i][j][0] += leftFalse * rightTrue
                    if not self.evaluate(0, 0, op):
                        dp[i][j][0] += leftFalse * rightFalse

        return dp[0][n - 1][1]  # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends