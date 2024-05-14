//{ Driver Code Starts
import java.io.*;
import java.util.*;

class IntMatrix {
    public static int[][] input(BufferedReader br, int n, int m) throws IOException {
        int[][] mat = new int[n][];

        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().trim().split(" ");
            mat[i] = new int[s.length];
            for (int j = 0; j < s.length; j++) mat[i][j] = Integer.parseInt(s[j]);
        }

        return mat;
    }

    public static void print(int[][] m) {
        for (var a : m) {
            for (int e : a) System.out.print(e + " ");
            System.out.println();
        }
    }

    public static void print(ArrayList<ArrayList<Integer>> m) {
        for (var a : m) {
            for (int e : a) System.out.print(e + " ");
            System.out.println();
        }
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            int rows;
            rows = Integer.parseInt(br.readLine());

            int columns;
            columns = Integer.parseInt(br.readLine());

            int[][] heights = IntMatrix.input(br, rows, columns);

            Solution obj = new Solution();
            int res = obj.MinimumEffort(rows, columns, heights);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends



class Solution {
    public static int MinimumEffort(int r, int c, int[][] h) {
        // code here
        PriorityQueue<List<Integer>>pq=new PriorityQueue<>((a,b) -> a.get(2).compareTo(b.get(2)));
        int directions[][]={{0,1},{0,-1},{1,0},{-1,0}};
        boolean visited[][]=new boolean[r][c];
        for(boolean row[]:visited)Arrays.fill(row,false);
        pq.add(List.of(0,0,0));
        
        while(!pq.isEmpty()){
            List<Integer>l=pq.poll();
            int x=l.get(0),y=l.get(1),maxEffort=l.get(2);
            if(x==r-1 && y==c-1)return maxEffort;
            visited[x][y]=true;
            for(int[] dir: directions){
                int tempX=x+dir[0];
                int tempY=y+dir[1];
                if(tempX>=0 && tempX<r && tempY>=0 && tempY<c && !visited[tempX][tempY]){
                    pq.add(List.of(tempX,tempY,Math.max(maxEffort,Math.abs(h[x][y]-h[tempX][tempY]))));
                }
            }
        }
        return -1;
}
}

