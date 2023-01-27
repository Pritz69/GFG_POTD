class Solution
{
    public static final int MOD = 1000000007;
    public int CountWays(String str)
    {
        int n = str.length();
        int[] dp = new int[n+1];
        dp[0] = 1;
        for(int i = 1;i<=n;i++){
            char curDigit = str.charAt(i-1);
            if(i < 2){
                //If first digit is 0 then string is invalid
                if(curDigit == '0'){
                    break;
                }
                else{
                    dp[i] = 1;
                }
            }
            else{
                char prevDigit = str.charAt(i-2);
                //If current digit is 0 and prev digit is greater than 3
                //Example : 30,40,50,60,70,80,90 then also string is invalid
                if(curDigit == '0' && prevDigit >= '3'){
                    break;
                }
                //Only include numbers from 1 to 9 as a single digit
                if(curDigit != '0'){
                    dp[i] = dp[i-1]%MOD;
                }
                //Check if two digit can be formed like 10-26
                if(prevDigit == '1' || (prevDigit == '2' && curDigit <= '6')){
                    dp[i] = (dp[i]%MOD + dp[i-2]%MOD)%MOD;
                }
            }
        }
        return dp[n];
    }
}
