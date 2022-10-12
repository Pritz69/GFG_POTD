class Solution{
public:
      string maxSum(string w,char x[], int b[],int n){
          // code here   
          if(w.length() == 1)   return w;
          
          vector<int> ascii(58, 0);
          int cnt = 65;
          for(int i=0;i<58;i++)    ascii[i] = cnt++;
          for(int i=0;i<n;i++)      ascii[x[i]-'A'] = b[i];
         
          int l = 0, r = 0, currMax = 0, max_ = 0;
          string res = "";
          while(r < w.length()){
               currMax += ascii[w[r]-'A'];

               if(currMax > max_)   max_ = currMax, res = w.substr(l, r-l+1);

               if(currMax < 0)      currMax = 0, l = r+1;
               r++;
          }
          
          return res;
      }
};
