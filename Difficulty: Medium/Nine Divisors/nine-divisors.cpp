class Solution {
  public:
    int countNumbers(int n) {
        int res = 0;
        for(int num=1;num*num <= n;num++){
            int cnt = 0;
            int sq = num*num;
            for(int i=1;i*i<=sq;i++){
                if(sq % i) continue;
                cnt++;
                if(sq/i != i) cnt++;
                if(cnt > 9) break;
            }
            if(cnt == 9) res++;
        }
        return res;
    }
};