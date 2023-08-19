    vector<int> subarraySum(vector<int>arr, int n, long long s)
    {
        // Your code here
       if(s==0)return {-1};
               
       int i=0,j=0,sum=0;
       while(j<=n){
           if(sum<s){
               sum+=arr[j];
               j++;
           }
           else if(sum==s){
               return {i+1,j}; 
           }
           else if(sum>s){
               sum-=arr[i];
               i++;
           }
       }
       return {-1};
    } 
