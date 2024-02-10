//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            
            int  k = Integer.parseInt(read.readLine());
            int  n = Integer.parseInt(read.readLine());
            int arr[][] = new int[n][n];
            String input_line1[] = read.readLine().trim().split("\\s+");
            int c = 0;
            for(int i=0;i<n;i++){
                for(int j = 0;j<n;j++){
                    arr[i][j] = Integer.parseInt(input_line1[c]);
                    c++;
                }
            }
            Solution obj = new Solution();
            System.out.println(obj.numberOfPath(n, k, arr));
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution {
    long numberOfPath(int n, int k, int [][]arr) {
        // code here
        return help(0, 0, n, k, arr, 0, 0);
    }

    long help(int rowIdx, int colIdx, int n, int k, int arr[][], long cnt, int sum){
        //rowIdx = 0, colIdx = 0 for first element
        if(rowIdx >= n || colIdx >= n){
            return cnt;
        }
        sum += arr[rowIdx][colIdx];
        // System.out.println(sum);
        if(sum > k){
            return cnt;
        }
        if(sum == k  && rowIdx == n-1 && colIdx == n-1){
            return cnt+1;
        }
        long r = help(rowIdx+1, colIdx, n, k, arr, cnt, sum);
        long c = help(rowIdx, colIdx+1, n, k, arr, cnt, sum);
        return r+c;

    }
}