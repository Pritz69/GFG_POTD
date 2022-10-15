class Solution {
   using pii=pair<int,int>;
    vector<vector<int>> dis={{0,-1},{-1,0},{0,1},{1,0}};
    bool isValid(int x,int y,int m,int n){
        return x>=0 and y>=0 and x<m and y<n;
    }
  public:
    int shortestPath(vector<vector<int>> &A, pair<int, int> source,
                     pair<int, int> destination) {
 int m=A.size(),n=A[0].size();
        queue<pii> q;
        q.push(source);
        A[source.first][source.second]=0;
        int k=0;
        while(q.size()){
            int len=q.size();
            while(len--){
                pii pair=q.front();q.pop();
                if(pair==destination) return k;
                auto i=pair.first,j=pair.second;
                for(auto &it:dis){
                    auto x=i+it[0];
                    auto y=j+it[1];
                    if(isValid(x,y,m,n) and A[x][y]){
                        q.push({x,y});
                        A[x][y]=0;
                    }
                }
            }
            k++;
        }
        return -1;
    }
};
