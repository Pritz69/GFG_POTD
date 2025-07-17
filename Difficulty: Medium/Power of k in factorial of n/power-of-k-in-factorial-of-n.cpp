class Solution {
  public:
    int maxKPower(int n, int k) {
        // Edge case: if k is 1, any number divides by 1 infinite times
        if (k == 1) return n; // or return a large number
        
        // Find prime factorization of k
        vector<pair<int, int>> primeFactors;
        int temp = k;
        
        // Check for factor 2
        if (temp % 2 == 0) {
            int count = 0;
            while (temp % 2 == 0) {
                count++;
                temp /= 2;
            }
            primeFactors.push_back({2, count});
        }
        
        // Check for odd factors from 3 onwards
        for (int i = 3; i * i <= temp; i += 2) {
            if (temp % i == 0) {
                int count = 0;
                while (temp % i == 0) {
                    count++;
                    temp /= i;
                }
                primeFactors.push_back({i, count});
            }
        }
        
        // If temp is still greater than 1, then it's a prime factor
        if (temp > 1) {
            primeFactors.push_back({temp, 1});
        }
        
        // Apply Legendre's formula for each prime factor
        int result = INT_MAX;
        
        for (auto& factor : primeFactors) {
            int prime = factor.first;
            int power = factor.second;
            
            // Count how many times 'prime' appears in n!
            int countInFactorial = 0;
            for (int p = prime; p <= n; p *= prime) {
                countInFactorial += n / p;
                // Check for overflow before next multiplication
                if (p > n / prime) break;
            }
            
            // How many complete sets of k can we form with this prime?
            int setsFromThisPrime = countInFactorial / power;
            
            // The answer is limited by the prime factor that gives minimum sets
            result = min(result, setsFromThisPrime);
        }
        
        return result;
    }
};