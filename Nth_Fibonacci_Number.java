class Solution {
    static int nthFibonacci(int n){
        // code here
        int a=1;
        int b=1;
        if (n==1 || n==2)
        {
            return 1;
        }
        int c=0;
        for(int i=3;i<=n;i++)
        {
            c=(a+b)%(1000000007);
            a=b%(1000000007);
            b=c%(1000000007);
        }
        return c%(1000000007);
    }
}
