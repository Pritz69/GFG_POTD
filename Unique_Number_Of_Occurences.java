class Solution {
    public static boolean isFrequencyUnique(int n, int[] arr) {
        // code here
        int maximumFrequency = 0;
        HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();

        for (int i = 0; i < n; i++) {
            int x = arr[i];
            int frequency = h.getOrDefault(x, 0);
            h.put(x, frequency + 1);
            maximumFrequency = Math.max(maximumFrequency, frequency + 1);
        }

        int[] c = new int[maximumFrequency + 1];
        for (int i : h.values()) {
            c[i]++;
            if (c[i] == 2) {
                return false;
            }
        }
        return true;
    }
}
        
