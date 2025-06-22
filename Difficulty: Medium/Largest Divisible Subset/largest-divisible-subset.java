class Solution {
    public ArrayList<Integer> largestSubset(int[] arr) {
        // code here
        int n = arr.length; 
        Arrays.sort(arr);
        
        for (int i = 0, j = arr.length - 1; i < j; i++, j--) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
        
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
 
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
 
        int maxSize = 1;
        int lastIndex = 0;
 
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (arr[j] % arr[i] == 0
                    && dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    parent[i] = j;
                }
            }
 
            if (dp[i] > maxSize) {
                maxSize = dp[i];
                lastIndex = i;
            }
        }
 
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = lastIndex; i >= 0; i = parent[i]) {
            res.add(arr[i]);
            if (parent[i] == -1)
                break;
        }
        return res;
        
    }
}