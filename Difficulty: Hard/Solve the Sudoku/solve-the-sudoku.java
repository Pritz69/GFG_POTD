//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = 9;
            int matrix[][] = new int[n][n];
            // String st[] = read.readLine().trim().split("\\s+");
            int k = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) matrix[i][j] = sc.nextInt();
            }
            Solution ob = new Solution();
            ob.solveSudoku(matrix);
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) System.out.print(matrix[i][j] + " ");
                System.out.println();
            }
            System.out.println("~");
        }
    }
}

// } Driver Code Ends


// User function Template for Java
class Solution {
    // Function to find a solved Sudoku.
    static boolean isSafe(int[][] mat, int row, int col, int digit) {
        
        for(int i=0; i<mat.length; i++)
        {
            if(mat[i][col] == digit || mat[row][i] == digit)
            return false;
        }
        
        int str = 3 * (row / 3);
        int stc = 3 * (col / 3);
        for(int i=str; i<str + 3; i++)
        {
            for(int j=stc; j<stc + 3; j++)
            {
                if(mat[i][j] == digit)
                return false;
            }
        }
        
        return true;
    }
    
    static boolean sudoku(int[][] mat, int row, int col) {
        
        if(row == mat.length)
        return true;
        
        int nextRow = row;
        int nextCol = col + 1;
        
        if(nextCol == mat.length)
        {
            nextRow = row + 1;
            nextCol = 0;
        }
        
        if(mat[row][col] != 0)
        return sudoku(mat, nextRow, nextCol);
        
        for(int digit=1; digit<=9; digit++)
        {
            if(isSafe(mat, row, col, digit))
            {
                mat[row][col] = digit;
                
                if(sudoku(mat, nextRow, nextCol))
                return true;
                
                mat[row][col] = 0;
            }
        }
        return false;
    }
    
    static void solveSudoku(int[][] mat) {
        // code here
        sudoku(mat, 0, 0);
        
    }
}


