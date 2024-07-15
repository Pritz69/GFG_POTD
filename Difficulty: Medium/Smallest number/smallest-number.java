//{ Driver Code Starts
import java.util.*;

class GFG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();

        while (tc-- > 0) {
            int s = sc.nextInt();
            int d = sc.nextInt();

            Solution obj = new Solution();
            String res = obj.smallestNumber(s, d);

            System.out.println(res);
        }
    }
}
// } Driver Code Ends



class Solution {
    public String smallestNumber(int s, int m) {
        // code here

      if(s> 9*m) return "-1";
      
      String str ="";
      
      s-=1;
      
      for(int i=m-1;i>=0;i--)
      {
          if(s>9){
              str+=9;
              s-=9;
          }
          else if(s<=9 && i>0){
             str+= s;
             s=0; 
          }
          else{
                str= str+(s+1);
          }
      }
      
    StringBuilder sb = new StringBuilder(str);
      
      return ""+sb.reverse();
   
    }
}
