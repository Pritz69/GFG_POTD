class Solution {
  public:
    int countConsec(int n) {
        // code here
        if(n == 2) return 1;
      
      int prev = 0 ;
      int curr = 1;
      int nex ;
      int ans = 1;
      for(int i = 3 ; i<=n ; i++){
          nex = prev+curr;
          ans =  ans * 2 + nex ; 
          prev = curr;
          curr = nex;
          
      }
      return ans ;
    }
};