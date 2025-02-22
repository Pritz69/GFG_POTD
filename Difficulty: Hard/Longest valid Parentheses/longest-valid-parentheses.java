//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while (t-- > 0) {
            String S = in.readLine();

            Solution ob = new Solution();
            System.out.println(ob.maxLength(S));

            System.out.println("~");
        }
    }
}
// } Driver Code Ends



class Solution {
    static int maxLength(String s) {
       int n=s.length();
       int l=0;
       int r=0;
       int max=0;
       for(int  i=0;i<n;i++)
       {
           if(s.charAt(i)=='(')
           l++;
           if(s.charAt(i)==')')
           r++;
           if(l==r)
           max=Math.max(max,2*l);
           if(r>l)
           {
               l=0;
               r=0;
           }
       }
       r=0;
       l=0;
       for(int i=n-1;i>=0;i--)
       {
           if(s.charAt(i)=='(')
           l++;
           if(s.charAt(i)==')')
           r++;
           if(l==r)
           max=Math.max(max,2*l);
           if(r<l)
           {
               l=0;
               r=0;
           }
       }
       return max;
    }
}