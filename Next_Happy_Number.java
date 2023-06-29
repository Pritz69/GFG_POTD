class Solution{

    static int nextHappy(int N){
        // code here
        int ans=N+1;
        while(true)
        {
            if (ishappy(ans))
            {
                return ans;
            }
            ans +=1;
        }
    }
    public static boolean ishappy(int n)
    {
        if (n==1 || n==7)
        {
            return true;
        }
        if (n>=2 && n<=9)
        {
            return false;
        }
        int s=0;
        while (n>0)
        {
            int d=n%10;
            s += d*d;
            n = n/10;
        }
        return ishappy(s);
    }
}
