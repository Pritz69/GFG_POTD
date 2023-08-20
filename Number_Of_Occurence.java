

//User function Template for Java



class Solution {
    int count(int[] arr, int n, int x) {
        // code here
        int l=0;
        int r=n-1;
        int lb=n;
        while(l<=r)
        {
            int m=(l+r)/2;
            if(arr[m]>=x)
            {
                lb=m;
                r=m-1;
            }
            else
            {
                l=m+1;
            }
        }
        l=0;
        r=n-1;
        int ub=n;
        while(l<=r)
        {
            int m=(l+r)/2;
            if(arr[m]>x)
            {
                ub=m;
                r=m-1;
            }
            else
            {
                l=m+1;
            }
        }
        return ub-lb;
    }
}
