#User function Template for python3

class Solution:
    def minSteps(self, d):
        # code here
        steps=0
        sum=0
        while (sum < d) :
            sum +=steps
            steps +=1
        #print(sum,steps)
        while ((sum-d)%2 !=0) :
            sum += steps
            steps +=1
        return steps-1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends