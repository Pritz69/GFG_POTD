//{ Driver Code Starts
import java.io.*;
import java.util.*;


class IntArray
{
    public static int[] input(BufferedReader br, int n) throws IOException
    {
        String[] s = br.readLine().trim().split(" ");
        int[] a = new int[n];
        for(int i = 0; i < n; i++)
            a[i] = Integer.parseInt(s[i]);

        return a;
    }

    public static void print(int[] a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }

    public static void print(ArrayList<Integer> a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            int n;
            n = Integer.parseInt(br.readLine());
            
            
            int k;
            k = Integer.parseInt(br.readLine());
            
            
            int[] arr = IntArray.input(br, n);
            
            Solution obj = new Solution();
            int res = obj.minimizeDifference(n, k, arr);
            
            System.out.println(res);
            
        }
    }
}

// } Driver Code Ends



class Solution {
    public static int minimizeDifference(int n, int k, int[] arr) {
        int post_max[] = new int[n];
        int post_min[] = new int[n];
        
        post_max[n - 1] = post_min[n - 1] = arr[n - 1];
        
        for(int i = n - 2; i >= 0; i--) {
            post_max[i] = Math.max(arr[i], post_max[i + 1]);
            post_min[i] = Math.min(arr[i], post_min[i + 1]);
        }
        
        int mini = arr[0], maxi = arr[0], res = post_max[k] - post_min[k];
        
        for(int i = 1; i < n - k; i++) {
            res = Math.min(res, Math.max(maxi, post_max[i + k]) - Math.min(mini, post_min[i + k]));
            mini = Math.min(mini, arr[i]);
            maxi = Math.max(maxi, arr[i]);
        }
        
        res = Math.min(res, maxi - mini);
        
        return res;
    }
}
        
