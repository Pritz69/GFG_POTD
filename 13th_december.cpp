vector<int> findRange(string s, int n) {
       vector<int>v(0);
       int f=0,sum=0,maxi=INT_MIN,end=0,start=0,st=0;
       for(auto x:s)
       { if(x=='0')
           { f=1;
               break;
           }
       }
       if(f==0) return {-1};
       for(int i=0;i<n;i++)
       { sum+=s[i]=='1'?-1:1;
           if(maxi<sum)
           {   maxi=sum;
               start=st;
               end=i;
           }
           if(sum<0)
           {   sum=0;
               st=i+1;
           }
       }
       v.push_back(start+1);
       v.push_back(end+1);
       return v;
    }
