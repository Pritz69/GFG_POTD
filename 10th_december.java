//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.io.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int N = Integer.parseInt(read.readLine());
            String str = read.readLine();
            Solution ob = new Solution();

            System.out.println(ob.buildLowestNumber(str,N));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    static String buildLowestNumber(String str, int k) {
        // code here
        Stack<Character> st=new Stack<>();
        for(char c:str.toCharArray()){
            while(!st.isEmpty() && st.peek()>c && k>0){
                st.pop();
                k--;
            }
            st.push(c);
        }

        while(!st.isEmpty() && k>0){
            st.pop();
            k--;
        }

        StringBuilder sb=new StringBuilder();
        while(!st.isEmpty()){
            sb.append(st.pop());
        }

        while(sb.length()>0 && sb.charAt(sb.length()-1)=='0'){
            sb.setLength(sb.length()-1);
        }
        if(sb.length()==0)return "0";
        return sb.reverse().toString();
    }
}
