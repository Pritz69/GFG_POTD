class Solution{
    public:
    vector<int> findLeastGreater(vector<int>& arr, int n) {
        vector<int>res(n,-1);
        set<int>s;
        s.insert(arr[n-1]);
        for(int i=n-2;i>=0;--i){
            auto j=s.upper_bound(arr[i]);
            if(j!=s.end()){
                res[i]=*j;}
            s.insert(arr[i]);}
        return res; 
    } };
