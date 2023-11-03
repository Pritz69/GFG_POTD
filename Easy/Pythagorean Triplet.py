class Solution {
    boolean checkTriplet(int[] arr, int n) {
        // code here
        if(n<3)
        {
            return false;
        }
        Arrays.sort(arr);
        int f=0;
        for(int i=n-1;i>=2;i--)
        {
            int l=0;
            int r=i-1;
            while (l<r)
            {
                long lv=arr[l]*arr[l];
                long rv=arr[r]*arr[r];
                long hp=arr[i]*arr[i];
                if ((lv+rv)==hp)
                {
                    return true;
                }
                if ( (lv+rv) < hp )
                {
                    l +=1;
                }
                else
                {
                    r -=1;
                }
            }
        }
        return false;
    }
}
