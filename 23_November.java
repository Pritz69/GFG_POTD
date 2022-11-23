class Solution {
    static long maxSumLCM(int n) {
        long sum = 0;

        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                sum += i;
                if (n / i != i) {
                    sum += (n / i);
                }
            }
        }

        return sum;
    }
}
