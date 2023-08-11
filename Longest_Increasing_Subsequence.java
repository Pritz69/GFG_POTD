
class Solution 
{
    //Function to find length of longest increasing subsequence.
    static int lbf(List<Integer> al,int target)
    {
        int l=0;
        int r=al.size()-1;
        int ans=0;
        while(l<=r)
        {
            int m=(l+r)/2;
            if(al.get(m)>=target)
            {
                ans=m;
                r=m-1;
            }
            else
            {
                l=m+1;
            }
        }
        return ans;
    }
    static int longestSubsequence(int size, int a[])
    {
        // code here
        List<Integer> al=new ArrayList<>();
        al.add(a[0]);
        for(int i=1;i<size;i++)
        {
            if(a[i]>al.get(al.size()-1))
            {
                al.add(a[i]);
            }
            else
            {
                int ind=lbf(al,a[i]);
                al.set(ind,a[i]);
            }
        }
        return al.size();
    }
} 
/*
class Solution 
{
    //Function to find length of longest increasing subsequence.
    static int longestSubsequence(int size, int a[])
    {
        // code here
        int dp[]=new int[size];
        int m=0;
        for(int i=0;i<size;i++)
        {
            dp[i]=1;
            for(int j=0;j<i;j++)
            {
                if (a[j]<a[i])
                {
                    dp[i]=Math.max(dp[i], 1+dp[j]);
                }
            }
            m=Math.max(m,dp[i]);
        }
        return m;
    }
}
*/
