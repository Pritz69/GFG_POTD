//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            String arr[] = br.readLine().split(" ");
            int a[] = new int[arr.length];

            for (int i = 0; i < arr.length; i++) {
                a[i] = Integer.parseInt(arr[i]);
            }
            Solution obj = new Solution();
            int f = 0;
            String A = obj.minSum(a);
            System.out.println(A);
            System.out.println("~");
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    String minSum(int[] arr) {
        // code here
        int n = arr.length;
        //sort the array
        Arrays.sort(arr);
        
        StringBuilder s1 = new StringBuilder();
        StringBuilder s2 = new StringBuilder();
        
        for(int i = 0 ; i < n ; i++){
            if(i % 2 == 0){
                //even index ,so number is added in sb1
                s1.append((char)(arr[i] + '0'));
            }else{
                //odd positon
                s2.append((char)(arr[i] + '0'));
            }
        } 
        
        //now add both them number 
        StringBuilder ans = new StringBuilder();
        int n1 = s1.length();
        int n2 = s2.length();  
        
        int i =  n1 - 1, j = n2 - 1 , carray = 0;
        while(i >= 0 && j >= 0){
            
            int d1 = s1.charAt(i--) - '0';
            int d2 = s2.charAt(j--) - '0'; 
            
            int sum = d1 + d2 + carray;
            
            ans.append((char)((sum % 10) + '0'));
            carray = sum / 10;
            
        }
        
        while(i >= 0){
           int d1 = s1.charAt(i--) - '0';
           int sum = d1 + carray;
           ans.append((char)((sum % 10) + '0'));
           carray = d1 / 10;
        }
        while(j >= 0){
           int d2 = s1.charAt(j--) - '0';
           int sum = d2 + carray;
           ans.append((char)((sum % 10) + '0'));
           carray = d2 / 10;
        }
        //if carray is not 0
        if(carray != 0) ans.append((char)(carray + '0'));
        //reverse ans  
        ans = ans.reverse(); 
        //any leading zeros remove it  
        while(ans.charAt(0) == '0'){
            ans = ans.deleteCharAt(0); 
        }   
        return ans.toString();
        
    }
}
