class Solution {
    public int nonLisMaxSum(int[] arr) {
        int n = arr.length;
        int[] dp = new int[n];

        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }

        int maxLen = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }

        boolean[] inLIS = new boolean[n];
        for (int i = n - 1; i >= 0; i--) {
            if (dp[i] == maxLen) {
                markLISHelper(i, arr, dp, inLIS, maxLen);
                break;
            }
        }

        int totalSum = 0;
        for (int i = 0; i < n; i++) {
            if (!inLIS[i]) {
                totalSum += arr[i];
            }
        }

        return totalSum;
    }

    private void markLISHelper(int i, int[] arr, int[] dp, boolean[] inLIS, int len) {
        if (len == 0) return;
        inLIS[i] = true;
        for (int j = i - 1; j >= 0; j--) {
            if (arr[j] < arr[i] && dp[j] == dp[i] - 1) {
                markLISHelper(j, arr, dp, inLIS, len - 1);
                break;
            }
        }
    }
}