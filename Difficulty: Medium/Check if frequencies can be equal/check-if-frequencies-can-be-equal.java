class Solution {
    boolean sameFreq(String s) {
        // code here
        Map<Integer,Integer>hm = new HashMap<>();
        int[] freq = new int[26];
        for (char c:s.toCharArray())
        {
            freq[c-'a']++;
        }
        
        for (int v:freq)
        {
            if (v!=0)
            {
                hm.put(v,hm.getOrDefault(v,0)+1);
            }
        }
        if (hm.size()==1) return true;
        if (hm.size()>2) return false;
        List<Integer>al=new ArrayList<>(hm.keySet());
        
        int a = al.get(0);
        int b=al.get(1);
        if (a==1 || b==1) return true;
        int max=Math.max(a,b);
        int min = Math.min(a,b);
        a=max;
        b=min;
        return Math.abs(a-b)==1 && hm.get(a)==1;
        
        
    }
}