

//User function Template for Java

class Solution{
    static long largestPrimeFactor(int N) {
        // code here
        long i=2;
        while ((i*i)<=N)
        {
            if (N%i==0)
            {
                N /= i;
            }
            else
            {
                i +=1;
            }
        }
        return N;
    }
}
