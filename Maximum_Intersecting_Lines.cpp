class Solution {
  public:
    int maxIntersections(vector<vector<int>> lines, int N) {
        // Code here
        map<int,int>mp;
        for(auto it:lines)
        {
            int s=it[0];
            int e=it[1];
            mp[s]+=1;
            mp[e+1]-=1;
        }
        int maxi=1;
        int prefixsum=0;
        for(auto it:mp)
        {
            prefixsum += it.second;
            maxi=max(maxi,prefixsum);
        }
        return maxi;
    }
};
