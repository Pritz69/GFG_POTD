//{ Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*;

// } Driver Code Ends
//User function Template for Java
class Solution{
    public int solve(int num1, int num2) {
        Set<Integer> vis = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        q.add(num1);
        vis.add(num1);

        int c = 0;

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int n = q.poll();
                if (n == num2) {
                    return c;
                }
                String nStr = Integer.toString(n);
                for (int j = 0; j < 4; j++) {
                    for (int k = 0; k < 10; k++) {
                        if (j == 0 && k == 0) {
                            continue;
                        }
                        String newStr = nStr.substring(0, j) + k + nStr.substring(j + 1);
                        int newNum = Integer.parseInt(newStr);
                        if (isPrime(newNum) && !vis.contains(newNum)) {
                            q.add(newNum);
                            vis.add(newNum);
                        }
                    }
                }
            }
            c++;
        }

        return -1; // If no solution is found
    }

    private boolean isPrime(int x) {
        if (x == 1) {
            return false;
        }
        if (x == 2 || x == 3) {
            return true;
        }
        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }
}

//{ Driver Code Starts.
class GFG{
    public static void main(String args[]) throws IOException{
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while(t-- > 0)
        {
            String input_line[] = read.readLine().trim().split("\\s+");
            int num1=Integer.parseInt(input_line[0]);
            int num2=Integer.parseInt(input_line[1]);
            
            Solution ob = new Solution();
            System.out.println(ob.solve(num1,num2));
        }
    }
}
// } Driver Code Ends