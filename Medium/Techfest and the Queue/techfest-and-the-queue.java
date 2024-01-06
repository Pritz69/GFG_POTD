//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            long a;
            a = Long.parseLong(br.readLine().trim());
            
            
            long b;
            b = Long.parseLong(br.readLine().trim());
            
            Solution obj = new Solution();
            long res = obj.sumOfPowers(a, b);
            
            System.out.println(res);
            
        }
    }
}

// } Driver Code Ends



class Solution {
    public static long sumOfPowers(long a, long b) {
        int s = 0;
        for (long i = a; i <= b; i++) {
            if (isPrime(i)) {
                s++;
            } else {
                long t = i;
                long n = i;
                long j = 2;
                while (j <= (Math.sqrt(t) + 2)) {
                    if (n % j == 0 && isPrime(j)) {
                        s++;
                        n = n / j;
                        if (isPrime(n)) {
                            s++;
                            break;
                        }
                    } else {
                        j++;
                    }
                }
            }
        }
        return s;
    }

    private static boolean isPrime(long x) {
        if (x == 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) {
                return false;
            }
        }
        return true;
    }
}
        
