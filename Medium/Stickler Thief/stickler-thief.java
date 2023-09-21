//{ Driver Code Starts
import java.util.*;
import java.io.*;

class GFG
 {
	public static void main (String[] args)
	 {
	  
	  //taking input using Scanner class
	  Scanner sc = new Scanner(System.in);
	  
	  //taking count of testcases
	  int t = sc.nextInt();
	  while(t-- > 0){
	      
	      //taking count of houses
	      int n = sc.nextInt();
	      int arr[] = new int[n];
	      
	      //inserting money present in 
	      //each house in the array
	      for(int i = 0; i<n; ++i)
	           arr[i] = sc.nextInt();
  	      
  	      //calling method FindMaxSum() of class solve
  	      System.out.println(new Solution().FindMaxSum(arr, n));
	 }
   }
}
// } Driver Code Ends


class Solution
{
    //Function to find the maximum money the thief can get.
    public int FindMaxSum(int[] a, int n) {
        // Create an array for memoization
        int[] dp = new int[n];
        Arrays.fill(dp, -1); // Initialize the array with -1 to indicate uninitialized values
        return rec(0, a, n, dp);
    }
    
    // Recursive function with memoization
    private int rec(int i, int[] a, int n, int[] dp) {
        if (i >= n) {
            return 0;
        }
        
        // Check if the result is already memoized
        if (dp[i] != -1) {
            return dp[i];
        }
                
        int take = a[i] + rec(i + 2, a, n, dp);
        int notTake = rec(i + 1, a, n, dp);
        
        // Store the result in the memoization array
        dp[i] = Math.max(take, notTake);
        
        return dp[i];
    }
}