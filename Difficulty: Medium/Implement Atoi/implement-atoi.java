//{ Driver Code Starts
// Initial template for JAVA

import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        while (t > 0) {
            String str = sc.nextLine();

            Solution obj = new Solution();
            int num = obj.myAtoi(str);
            System.out.println(num);
            System.out.println("~");
            t--;
        }
    }
}
// } Driver Code Ends

class Solution {
    public int myAtoi(String s) {
        s=s.trim();
        boolean neg = false;
        int i=0;
        if(s.charAt(0) == '-'){
            neg = true;
            i=1;
        }
        
        long res = 0;
        
        for(;i<s.length();i++){
            if(!Character.isDigit(s.charAt(i))){
                return neg ? (int)(res)*-1 : (int)res;
            }
            
            res = res*10+(s.charAt(i)-'0');
        }
        if(neg && res*-1 < Integer.MIN_VALUE){
            return Integer.MIN_VALUE;
        }
        if(res > Integer.MAX_VALUE){
            return Integer.MAX_VALUE;
        }
        
        return neg ? (int)(res)*-1 : (int)res;
    }
}