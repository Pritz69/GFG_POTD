//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            int N = Integer.parseInt(in.readLine().trim());
            
            Solution ob = new Solution();
            List<Integer> ans = new ArrayList<Integer>();
            ans = ob.pattern(N);
            for(int i = 0;i < ans.size();i++)
                System.out.print(ans.get(i) + " ");
            System.out.println();
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution{
    public List<Integer> pattern(int N) {
        List<Integer> result = new ArrayList<>();
        fn(N, result);
        int n=result.size();
        for(int i=n-2;i>=0;i--)
        {
            result.add(result.get(i));
        }
        return result;
    }
    private void fn(int n, List<Integer> l) 
    {
        if (n <= 0) 
        {
            l.add(n);
            return ;
        } 
        else 
        {
            l.add(n);
            fn(n - 5, l);
        }
    }
}