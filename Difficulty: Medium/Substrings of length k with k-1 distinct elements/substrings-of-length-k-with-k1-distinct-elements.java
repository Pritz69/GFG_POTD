class Solution {
    public int substrCount(String s, int k) {
        // code here
        int ans=0;
        int l=0;
        int n=s.length();
        int r=0;
        HashMap<Character,Integer> hash=new HashMap<>();
        while (r<n)
        {
            char c=s.charAt(r);
            hash.put(c, hash.getOrDefault(c, 0) + 1);
            while ((r-l+1)>k) 
            {
                char cc=s.charAt(l);
                hash.put(cc, hash.getOrDefault(cc, 0) - 1);
                if (hash.get(cc)==0)
                {
                    hash.remove(cc);
                }
                l+=1;
            }
            if ((r-l+1==k) && (hash.size()==k-1))
            {
                ans +=1;
            }
            r +=1;
        }
        return ans;
    }
}