class Solution {
    public boolean divby13(String s) {
        // code here
        int rem = 0;
        for (int i = 0; i < s.length(); i++) {
            rem = (rem * 10 + (s.charAt(i) - '0')) % 13;
        }
        return rem == 0;
    }
}