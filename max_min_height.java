class Solution{
	static boolean possible(int n,int a[],int k,int w,int mid){
        int arr[] = new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=a[i];
        }
        for(int i=0;i<n;i++){
            if(arr[i]<mid){
                int temp = mid-arr[i];
                if(temp>k)return false;
                k-=temp;
                arr[i]=mid;
                for(int j=i+1;j<n && j<i+w;j++){
                    arr[j]+=temp;
                }
            }
        }
        return true;
    }
	long maximizeMinHeight(int N, int K, int W,int [] a)
    {
        //Write your code here
        int mn=Integer.MAX_VALUE,mx;
        for(int i=0;i<N;i++)mn=Math.min(mn,a[i]);
        mx=mn+K;
        long ans=0;
        while(mn<=mx){
            int mid = (mn+mx)/2;
            if(possible(N,a,K,W,mid)){
                ans=mid;
                mn=mid+1;
            }
            else mx=mid-1;
        }
        return ans;
    }
}
