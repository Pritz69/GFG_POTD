//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int arr[] = new int[s.length];
            for (int i = 0; i < s.length; i++) {
                arr[i] = Integer.parseInt(s[i]);
            }

            int[] ans = new Solution().constructLowerArray(arr);
            for (int i = 0; i < arr.length; i++) {
                System.out.print(ans[i] + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


// User function Template for Java
class Solution {
    int[] constructLowerArray(int[] arr) {
        // code here
        int n = arr.length;
        int ans[] = new int[n];
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=n-1;i>=0;i--){
            if(list.isEmpty() || list.get(list.size()-1) < arr[i]){
                ans[i] = list.size();
                list.add(arr[i]);
            }else{
                int index = -1;
                int low = 0,high = list.size()-1;
                while(low<=high){ 
                    int mid = low+(high-low)/2;
                    if(arr[i]>list.get(mid)){
                        index = mid;
                        low = mid+1;
                    }else {
                        high=mid-1;
                    }
                }
                ans[i] = index+1;
                list.add(index+1,arr[i]);
            }
        }
        return ans;
    }
}


