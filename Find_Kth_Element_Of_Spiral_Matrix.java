class Solution
{
    /*You are required to complete this method*/
    int findK(int A[][], int n, int m, int k)
    {
	// Your code here	
	int c=0;
	int l=0;
	int r=m-1;
	int t=0;
	int b=n-1;
	while (l <=r && t <=b) 
	{
	    for (int i=l;i<=r;i++)
	    {
	        c ++;
	        if (c==k)
	        {
	            return A[t][i];
	        }
	    }
	    t++;
	    for (int i=t;i<=b;i++)
	    {
	        c ++;
	        if (c==k)
	        {
	            return A[i][r];
	        }
	    }
	    r--;
	    if (t<=b)
	    {
	        for (int i=r;i>=l;i--)
	        {
	        c ++;
	        if (c==k)
	        {
	            return A[b][i];
	        }
	        }
	        b--;
	    }
	    if (l<=r)
	    {
	        for (int i=b;i>=t;i--)
	        {
	        c ++;
	        if (c==k)
	        {
	            return A[i][l];
	        }
    	    }
    	    l++;
	    }
	}
	return 0;
    }
}
