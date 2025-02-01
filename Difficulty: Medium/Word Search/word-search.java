//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt(); // Number of test cases
        while (tc-- > 0) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            char[][] mat = new char[n][m];

            // Reading the matrix
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    mat[i][j] = sc.next().charAt(0);
                }
            }

            String word = sc.next();
            Solution obj = new Solution();
            boolean ans = obj.isWordExist(mat, word);
            if (ans)
                System.out.println("true");
            else
                System.out.println("false");

            System.out.println("~");
        }
        sc.close();
    }
}
// } Driver Code Ends


class Solution {
    static public boolean isWordExist(char[][] mat, String word) {
        // Code here
        for(int i=0;i<mat.length;i++){
            for(int j=0; j<mat[i].length; j++){
                if(mat[i][j]==word.charAt(0)){
                    if(checkIfExists(mat, i, j, word, 0)){
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    static boolean checkIfExists(char[][] mat,int i, int j, String word, int idx){
        if(idx == word.length()){
            return true;
        }
        if(i<0 || j<0 || i>=mat.length || j>=mat[0].length){
            return false;
        }
        if(mat[i][j] == word.charAt(idx)){
            mat[i][j] = '-';
           boolean ans = checkIfExists(mat, i+1, j, word, idx+1) || 
           checkIfExists(mat, i-1, j, word, idx+1) ||
           checkIfExists(mat, i, j+1, word, idx+1) ||
           checkIfExists(mat, i, j-1, word, idx+1); 
           mat[i][j] = word.charAt(idx);
           return ans;
           
        } else {
            return false;
        }
    }
}