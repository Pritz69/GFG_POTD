

//User function Template for Java

class Solution
{
    public long findMinDiff (ArrayList<Integer> a, int n, int m)
    {
        // your code here
        Collections.sort(a);
        int min=Integer.MAX_VALUE;        
        int l=0;
        int r=m-1;
        while(r < n)
        {
            min=Math.min(min,a.get(r)-a.get(l));
            l +=1;
            r +=1;
        }
        return min;
    }
}
