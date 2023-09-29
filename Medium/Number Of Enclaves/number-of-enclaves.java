//{ Driver Code Starts
// Initial Template for Java

// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

// Position this line where user code will be pasted.

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
        int T = Integer.parseInt(in.readLine());
        while (T-- > 0) {
            String s[] = in.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int m = Integer.parseInt(s[1]);
            int a[][] = new int[n][m];
            for (int i = 0; i < n; i++) {
                s = in.readLine().trim().split(" ");
                for (int j = 0; j < m; j++) {
                    a[i][j] = Integer.parseInt(s[j]);
                }
            }
            Solution ob = new Solution();
            out.println(ob.numberOfEnclaves(a));
        }
        out.close();
    }
}
// } Driver Code Ends


// User function Template for Java
class Pair
{
    int x;
    int y;
    public Pair(int x,int y)
    {
        this.x=x;
        this.y=y;
    }
}
class Solution {
    int numberOfEnclaves(int[][] grid) {
        // Your code here
        int n=grid.length;
        int m=grid[0].length;
        Queue<Pair> q=new LinkedList<Pair>();
        int vis[][]=new int[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if (i==0 || j==0 || i==n-1 || j==m-1)
                {
                    if (grid[i][j]==1)
                    {
                        vis[i][j]=1;
                        q.add(new Pair(i,j));
                    }
                }
            }
        }
        int dr[]={-1,0,1,0};
        int dc[]={0,1,0,-1};
        while (!q.isEmpty())
        {
            int r=q.peek().x;
            int c=q.peek().y;
            q.remove();
            for(int i=0;i<4;i++)
            {
                int nr=r+dr[i];
                int nc=c+dc[i];
                if (nr >=0 && nr<n && nc >=0 && nc < m && vis[nr][nc]==0 && grid[nr][nc]==1)
                {
                    q.add(new Pair(nr,nc));
                    vis[nr][nc]=1;
                }
            }
        }
        int c=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                if ( vis[i][j]==0 && grid[i][j]==1 )
                {
                    c +=1;
                }
            }
        }
        return c;
    }
}