//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String str1 = sc.next();
            String str2 = sc.next();

            Solution obj = new Solution();
            String ans = obj.betterString(str1, str2);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    public static String betterString(String str1, String str2) {
        // Count the number of substrings of each string
        int a = countSub(str1);
        int b = countSub(str2);
        
        // Return the string with more substrings
        if (a < b) {
            return str2;
        }
        return str1;
    }
    
    
    static int countSub(String str) {
        // map to store the last occurrence of characters
      Map<Character, Integer> map = new HashMap<>();
       
        int n = str.length();
        int[] dp = new int[n + 1];

        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            
            dp[i] = 2 * dp[i - 1];

            if (map.containsKey(str.charAt(i - 1))) {
                dp[i] = dp[i] - dp[map.get(str.charAt(i - 1))];
            }
            map.put(str.charAt(i - 1), (i - 1));
        }
        return dp[n];
    }
}