class Solution
{
    public:
        void merge_sort(int arr[], int low, int mid, int high){
            int i = low, j = mid+1;
            vector<int> cur;
            while(i<=mid && j<=high){
                if(arr[i] < 0 || (arr[i]>=0 && arr[j]>=0)){
                    cur.push_back(arr[i]);
                    i++;
                }
                else{
                    cur.push_back(arr[j]);
                    j++;
                }
            }
            while(i<=mid){
                cur.push_back(arr[i]);
                i++;
            }
            while(j<=high){
                cur.push_back(arr[j]);
                j++;
            }
            for(int k = low; k<=high; k++){
                arr[k] = cur[k-low];
            }
        }
        void merge(int arr[], int low, int high){
            if(low<high){
                int mid = (high+low)/2;
                merge(arr,low,mid);
                merge(arr,mid+1,high);
                merge_sort(arr,low,mid,high);
            }
        }
        void Rearrange(int arr[], int n)
        {
            // Your code goes here
            int low = 0, high = n-1;
            merge(arr,low,high);
}
};
