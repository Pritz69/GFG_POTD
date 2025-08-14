class Solution {
  public:
    int cnt=0;
 void merge(int low,int mid,int high,vector<int>& a){
    vector<int> temp;
    int left=low;
    int right=mid+1;
    while(left<=mid && right<=high){
        if(a[left]<=a[right]){
            temp.push_back(a[left]);
            left++;
        }
        else{
            temp.push_back(a[right]);
            right++;
        }
    }
    while(left<=mid){
         temp.push_back(a[left]);
            left++;
    }
    while(right<=high){
         temp.push_back(a[right]);
            right++;
    }
      for(int i=low;i<=high;i++){
        a[i]=temp[i-low];
      }

    return;
}

void countpairs(int low,int mid,int high,vector<int>& a){
    int right=mid+1;
    for(int i=low;i<=mid;i++){
        while(right<=high && a[i]>2*(long long)a[right]){
            right++;
        }
        cnt+=(right-(mid+1));
    }
    return;

}

void mergeSort(int low,int high,vector<int>& a,int n){
    if(low>=high)return;
    int mid=(low+high)>>1;
    mergeSort(low,mid,a,n);
    mergeSort(mid+1,high,a,n);
    countpairs(low,mid,high,a);
    merge(low,mid,high,a);
    return;
}
    int countRevPairs(vector<int> &arr) {
        // Code here
         int n=arr.size();
        mergeSort(0,n-1,arr,n);
        return cnt;
        
    }
};