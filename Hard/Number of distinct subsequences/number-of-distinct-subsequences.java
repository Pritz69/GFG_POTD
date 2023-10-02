//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String s = read.readLine();
            Solution ob = new Solution();
            System.out.println(ob.distinctSubsequences(s));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    int distinctSubsequences(String S) {
        // code here
        int n=S.length();
        int mod=1000000007;
        HashMap<Character,Integer> mp=new HashMap<>(); 
        int dp[]=new int[n+1];
        dp[0]=1;
        for(int i=1;i<=n;i++)
        {
            char s=S.charAt(i-1);
            dp[i]=(dp[i-1]*2) % mod;
            if (mp.containsKey(s))
            {
                dp[i]=(dp[i]-dp[mp.get(s)-1]+ mod) % mod;
            }
            mp.put(s,i);
        }
        return dp[n];
    }
}