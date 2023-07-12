
class Solution
{
        
    long power(int N,int R)
    {
        //Your code here
        int mod=1000000007;
        long ans=0;
        if (R==0)
        {
            return 1;
        }
        if (R%2 ==0)
        {
            ans = power(N,R/2)%mod;
            ans = (ans * ans)%mod ;
        }
        else
        {
            ans = N % mod;
            ans = (ans * power(N,R-1)%mod)%mod;
        }
        return ans % mod;
        
    }

}
