
class Solution{
    static String longestPalin(String s){
        // code here
        String res = "";
        int reslen = 0;
        int res_l=0;
        int res_r=0;
        for (int i = 0; i < s.length(); i++) {
            int l = i, r = i;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > reslen) {
                    res_l=l;
                    res_r=r+1;
                    reslen = r - l + 1;
                }
                l--;
                r++;
            }
            l = i;
            r = i + 1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > reslen) {
                    res_l=l;
                    res_r=r+1;
                    reslen = r - l + 1;
                }
                l--;
                r++;
            }
        }
        return s.substring(res_l,res_r);
        
    }
}
