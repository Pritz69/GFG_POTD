//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int r = sc.nextInt();
            int c = sc.nextInt();

            int matrix[][] = new int[r][c];

            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) matrix[i][j] = sc.nextInt();
            }
            Solution ob = new Solution();
            ArrayList<Integer> ans = ob.spirallyTraverse(matrix);
            for (Integer val : ans) System.out.print(val + " ");
            System.out.println();
        }
    }
}
// } Driver Code Ends


class Solution {
    // Function to return a list of integers denoting spiral traversal of matrix.
    public ArrayList<Integer> spirallyTraverse(int matrix[][]) {
        // code here
        ArrayList<Integer>list=new ArrayList<>();
        int r=matrix.length;
        int c=matrix[0].length;
       
        int sr=0;
        int er=r-1;
        int sc=0;
        int ec=c-1;
        
       while(sr<=er && sc<=ec)
       {
      
         for(int j=sc;j<=ec;j++)
         {
             list.add(matrix[sr][j]);
         }
         sr++;
     
         for(int i=sr;i<=er;i++)
         {
             list.add(matrix[i][ec]);
         }
         ec--;
         
          if(sr<=er)
           {
                 for(int j=ec;j>=sc;j--){
                 list.add(matrix[er][j]);
            }
               er--;
          
           }
     
        if(sc<=ec)
        {
             for(int i=er;i>=sr;i--){
             list.add(matrix[i][sc]);
            }
        }
               
        sc++;
        }
       
       return list;
     
    }
}
