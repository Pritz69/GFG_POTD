class Solution{
    static int rec(int ind,int target,int dp[][],int N,int arr[])
    {
        if(target==0)
        {
            return 1;
        }
        if (ind==N)
        {
            return 0;
        }
        if (dp[ind][target] != -1) 
        {
            return dp[ind][target];
        }
        int take=0;
        if (arr[ind]<=target)
        {
            take=rec(ind+1,target-arr[ind],dp,N,arr);
        }
        int nottake=rec(ind+1,target,dp,N,arr);
        
        dp[ind][target]=take | nottake;
        return dp[ind][target];
    }
    static int equalPartition(int N, int arr[])
    {
        // code here
        int s=0;
        for (int x:arr)
        {
            s +=x;
        }
        if(s%2==1)
        {
            return 0;
        }
        int tar=s/2;
        int dp[][]=new int[N][tar+1];
        for (int a[]:dp)
        {
            Arrays.fill(a,-1);
        }
        return rec(0,tar,dp,N,arr);
    }
}

# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        def f(ind, target):
            if target==0:
                return True
            if ind==0:
                if arr[ind]==target:
                    return True
                return False
            if dp[ind][target]!=-1:
                return dp[ind][target]
            notp=f(ind-1,target)
            pick=0
            if arr[ind]<=target:
                pick=f(ind-1,target-arr[ind])
            dp[ind][target]=pick or notp
            return dp[ind][target]
        
        s=sum(arr)
        if s%2!=0:
            return False
        target=s//2
        dp=[[-1]*(target+1) for _ in range(N)]
        return f(N-1,target)


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends
