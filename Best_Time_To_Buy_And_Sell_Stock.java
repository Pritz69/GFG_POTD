
class Solution {
    public static int stockBuyAndSell(int n, int[] prices) {
        // code here
        int ans=0;
        if (n==0)
        {
            return 0;
        }
        for (int i=0;i<n-1;i++)
        {
            if (prices[i] < prices[i+1])
            {
                ans += prices[i+1]-prices[i];
            }
        }
        return ans;
    }
}
        
