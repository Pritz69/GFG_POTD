class Solution{
public:
    int isPossible(int n, int m, string s){
        // code here
        int l=0,r=0,u=0,d=0;
        int x=0;
        int y=0;
       for(int i=0;i<s.size();i++)
       {
           if(s[i]=='L'){
               l=min(l,--x);
           }
          else  if(s[i]=='R'){
               r=max(r,++x);
           }
          else  if(s[i]=='U'){
               u=max(u,++y);
           }
          else if(s[i]=='D'){
               d=min(d,--y);
           }
       }
       if(r-l>=m||u-d>=n)return 0;
       return 1;
    }
};
