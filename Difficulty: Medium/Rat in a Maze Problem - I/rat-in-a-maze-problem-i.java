//{ Driver Code Starts
// Initial Template for Java

import java.util.*;

class Rat {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();
            int[][] a = new int[n][n];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++) a[i][j] = sc.nextInt();

            Solution obj = new Solution();
            ArrayList<String> res = obj.findPath(a);
            Collections.sort(res);
            if (res.size() > 0) {
                for (int i = 0; i < res.size(); i++) System.out.print(res.get(i) + " ");
                System.out.println();
            } else {
                System.out.println(-1);
            }
        }
    }
}

// } Driver Code Ends


class Solution {
    public ArrayList<String> paths = new ArrayList<>();
    public void dfs(int x,int y,String path,int n,int[][] mat){
        if (x==n-1 && y==n-1){
            paths.add(path);
            return;
        }
        mat[x][y] =0;
        String[] moves = {"R", "L", "U", "D"};
        int[][] directions = {
            {0, 1},   // R: Right (x, y + 1)
            {0, -1},  // L: Left (x, y - 1)
            {-1, 0},  // U: Up (x - 1, y)
            {1, 0}    // D: Down (x + 1, y)
        };

        // Iterate through the directions
        for (int i = 0; i < directions.length; i++) {
            String move = moves[i];
            int dx = directions[i][0];
            int dy = directions[i][1];
            int nx = x + dx;
            int ny = y + dy;
            if ((0<=ny && ny<n) && (0<=nx && nx<n) &&(mat[nx][ny]==1)){
                dfs(nx,ny,path+move,n,mat);
            }
        }
        mat[x][y]=1;
        
    }
    public ArrayList<String> findPath(int[][] mat) {
        // Your code here
        int n = mat.length;
        if(mat[n-1][n-1]== 0 || mat[0][0]==0){
            ArrayList<String> no = new ArrayList<String>();
            return no;
        }
        dfs(0,0,"",n,mat);
        return paths;
    }
}