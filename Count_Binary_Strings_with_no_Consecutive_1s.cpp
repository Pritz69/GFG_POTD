// User function Template for C++
class Solution {
  public:
    const int MOD = 1e9+7;
    int countStrings(long long int N)
    {
    vector<vector<int>> matrix = {{1, 1}, {1, 0}};
    vector<vector<int>> res = matrixPower(matrix, N);
    return res[0][0];
    }
    vector<vector<int>> multiplyMatrices(vector<vector<int>>& a, vector<vector<int>>& b)
    {
        vector<vector<int>> result(2, vector<int>(2));    // matrix zero
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    result[i][j] = (result[i][j] + (long long)a[i][k] * b[k][j]) % MOD;
                }
            }
        }
        return result;
    }
    vector<vector<int>> matrixPower(vector<vector<int>>& a, long long n) 
    {
        vector<vector<int>> result = {{1, 1}, {1, 0}};  
        while (n > 0) {
            if (n % 2 == 1) {
                result = multiplyMatrices(result, a);
            }
            a = multiplyMatrices(a, a);
            n /= 2;
        }
        return result;
    }
};
