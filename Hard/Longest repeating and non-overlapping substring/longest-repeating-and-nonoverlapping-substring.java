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
            int N = Integer.parseInt(read.readLine());
            String S = read.readLine();

            Solution ob = new Solution();
            System.out.println(ob.longestSubstring(S, N));
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution {
    static String longestSubstring(String s, int n) {
        String res = "";
        int i=0, j=0;
        
        while(j < n && i < n) {
            String str = s.substring(i, j+1);
            if(s.substring(j+1, n).indexOf(str) != -1) 
                res = res.length() < (j-i+1) ? str : res;
            else
                i++;
            j++;
        }
        return res == "" ? "-1" : res;
    }
};


