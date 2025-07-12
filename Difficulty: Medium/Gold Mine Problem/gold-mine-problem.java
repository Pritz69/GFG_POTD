class Solution {
    
    public int maxGold(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        Map<String, Integer> dp = new HashMap<>();

        int maxGold = 0;
        for (int i = 0; i < n; i++) {
            maxGold = Math.max(maxGold, func(i, 0, mat, n, m, dp));
        }

        return maxGold;
    }

    private int func(int i, int j, int[][] mat, int n, int m, Map<String, Integer> dp) {
        String key = i + "," + j;

        if (dp.containsKey(key)) {
            return dp.get(key);
        }

        if (i < 0 || i >= n || j >= m) {
            return 0;
        }

        int ans = 0;

        // Move right-up
        if (i - 1 >= 0) {
            ans = Math.max(ans, mat[i][j] + func(i - 1, j + 1, mat, n, m, dp));
        }

        // Move right-down
        if (i + 1 < n) {
            ans = Math.max(ans, mat[i][j] + func(i + 1, j + 1, mat, n, m, dp));
        }

        // Move right
        ans = Math.max(ans, mat[i][j] + func(i, j + 1, mat, n, m, dp));

        dp.put(key, ans);
        return ans;
    }
}