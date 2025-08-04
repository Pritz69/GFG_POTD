class Solution {
  public:
  
    // Standard Kadane's Algorithm for 1D max subarray sum
    int kadanes(vector<int>& arr) {
        int n = arr.size();
        int maxsum = arr[0];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
            maxsum = max(maxsum, sum);
            if (sum < 0) sum = 0;
        }
        return maxsum;
    }

    int maxRectSum(vector<vector<int>> &mat) {
        int n = mat.size();
        int m = mat[0].size();
        int maxsum = INT_MIN;

        // Fix left column
        for (int left = 0; left < m; left++) {
            vector<int> temp(n, 0);

            // Move right column from left to end
            for (int right = left; right < m; right++) {
                // Accumulate row-wise sums between columns
                for (int i = 0; i < n; i++) {
                    temp[i] += mat[i][right];
                }

                // Find the best subarray sum for current column range
                int sum = kadanes(temp);
                maxsum = max(maxsum, sum);
            }
        }

        return maxsum;
    }
};
