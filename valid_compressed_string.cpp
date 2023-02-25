class Solution {
  public:
       int checkCompressed(string S, string T) {
        // code here
        int num=0,j=0;
        for(int i=0;i<T.length();i++){
            if(isdigit(T[i])){
                num = num*10+(T[i]-'0');
            }
            else{
                if(num){
                    j+=num;
                }
                num=0;
                if(j>=S.length() or S[j]!=T[i])return 0;
                j++;
            }
        }
        j+=num;
        if(j!=S.length())return 0;
        return 1;
    }
};
