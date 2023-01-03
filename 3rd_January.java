class Solution {
    public int removeStudents(int[] H, int N) {
        // code here
        int m=0;
        m=longestSubsequence(N,H);
        int ans=0;
        ans=N-m;
        return (ans);
    }
    static int longestSubsequence(int size, int arr[])
    {
        // using binary search
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(arr[0]);
        int len = 1;
        for (int i = 1; i < size; i++) {
            if (arr[i] > ans.get(ans.size() - 1)) {
                ans.add(arr[i]);
                len++;
            } else {
                int indx = binarySearch(ans, arr[i]);
                ans.set(indx, arr[i]);
            }
        }
        return len;
    }
    
    static int binarySearch(ArrayList<Integer> ans, int key) {
        int low = 0;
        int high = ans.size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (ans.get(mid) == key) return mid;
            else if (ans.get(mid) < key) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high + 1;
    }
};
