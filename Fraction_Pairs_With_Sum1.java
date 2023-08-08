class Solution {
    public static int countFractions(int n, int[] numerator, int[] denominator) {
        // code here
        
        Map<Double,Integer> mp = new HashMap<>();
        int count=0;
        for(int i=0; i<n; i++) 
        {
            double fract = (double)numerator[i]/(double)denominator[i];
            double x = (double)(denominator[i]-numerator[i])/denominator[i];
            count += mp.getOrDefault(x, 0);
            mp.put(fract, mp.getOrDefault(fract, 0) + 1);
        }
        return count;
    }
}
