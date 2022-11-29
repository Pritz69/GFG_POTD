class Solution {
    
    public static int numoffbt(int arr[], int n)
    {
         // Your code goes here
         int min=Integer.MAX_VALUE;
         int max=1;
         for(int i:arr)
         {
             min=Math.min(min,i);
             max=Math.max(max,i);
         }
         int []dp=new int[max+1];
         for(int i:arr)
         {
             dp[i]=1;
         }
         int ans=0;
         for(int i=min;i<=max;i++)
         {
             if (dp[i]!=0)
             {
                 for(int j=i+i;j<=max &&(j/i)<=i;j+=i)
                 {
                     if (dp[j]!=0)
                     {
                         dp[j]+=(dp[i]*dp[j/i]);
                         if(i != (j/i))
                         {
                             dp[j]+=(dp[i]*dp[j/i]);
                         }
                     }
                 }
                 ans+=dp[i]%1000000007;
             }
         }
         return ans%1000000007;
    }
}
