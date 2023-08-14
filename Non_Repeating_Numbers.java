

//User function Template for Java

class Solution
{
    public int[] singleNumber(int[] nums)
    {
        // Code here
        int x=0;
        for(int n:nums)
        {
            x=x^n;
        }
        int rightmostbit= (x&(x-1))^x ;
        int a[]=new int[2];
        for(int n:nums)
        {
            if((rightmostbit&n) !=0)
            {
                a[0]=a[0]^n;
            }
            else
            {
                a[1]=a[1]^n;
            }
        }
        if (a[0]>a[1])
        {
            int t=a[0];
            a[0]=a[1];
            a[1]=t;
        }
        return a;
    }
}
