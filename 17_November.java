class Solution {

    long countSubarray(int arr[], int n, int k) {

        // code here
        int recent=-1;
        long ans=0;
        for(int i=0;i<n;i++)
        {
            if(arr[i]>k)
            {
              ans++;
              int left=i-(recent+1);
              ans+=left;
              int right=n-1-i;
              ans+=right;
              int center=(left*right);
              ans+=center;
              recent=i;
            }
        }
        return ans;
    }
}
