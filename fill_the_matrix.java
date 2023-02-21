class Solution
{
	public static int minIteration(int N, int M, int x, int y){
		//code here
		int dist=0;
        int max=Integer.MIN_VALUE;
		for(int i=0;i<N;i++)
	    {
	     for(int j=0;j<M;j++)
	     {
	         dist=Math.abs(i+1-x)+Math.abs(j+1-y);
	         max=Math.max(dist,max);
	     }
	    }
	    return max;
	}
}
