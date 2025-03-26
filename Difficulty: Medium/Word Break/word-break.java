//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class GfG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        while (t-- > 0) {
            String s = sc.nextLine();
            String line = sc.nextLine();
            String[] dictionary = line.split(" ");

            Solution obj = new Solution();
            if (obj.wordBreak(s, dictionary)) {
                System.out.println("true");
            } else {
                System.out.println("false");
            }
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


class Solution {
    public boolean wordBreak(String s, String[] dictionary) {
        // code here
        int n = s.length();
        
        int[] dp = new int[n+1];
        
        dp[0] = 1;
        
        for(int i=1; i<=n; i++){
            for(String str : dictionary){
                int start = i - str.length();
                if(start >= 0 && dp[start] == 1 && s.substring(start, i).equals(str)){
                    dp[i] = 1;
                    break;
                }
            }
        }
        
        if(dp[n]==1)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}