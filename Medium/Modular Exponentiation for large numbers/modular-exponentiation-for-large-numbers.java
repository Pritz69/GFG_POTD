//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String s = br.readLine();
            String[] S = s.split(" ");
            long x = Long.parseLong(S[0]);
            long n = Long.parseLong(S[1]);
            long m = Long.parseLong(S[2]);
            Solution ob = new Solution();
            long ans = ob.PowMod(x, n, m);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
    public long PowMod(long x, long n, long m)
    {//exponentiation by squaring method -
        if(n == 0) return (1 % m);
        if(n == 2) return (x * x)% m;
        long ans = 1l;//stores the ans
        long sq = x;//helps to update the ans
        while(n > 0){
            if(n % 2 == 1){//if our power is odd, we update the ans by multiplying with sq
                ans = (ans * sq)% m;
            }
            sq = (sq * sq) % m;//we keep on updating the sq
            n = n / 2;//and dividing by 2
        }
        return ans % m;
    }
}