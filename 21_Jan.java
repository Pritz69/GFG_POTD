class Solution {
    public static int minVal(int a, int b) {
        int bitsA=Integer.bitCount(a);
        int bitsB=Integer.bitCount(b);
        int diff=Math.abs(bitsA-bitsB);
        
        if(diff==0)return a;
        else if(bitsA>bitsB){
            while(diff>0){
                a = a&(a-1);
                diff--;
            }
        }else{
            while(diff>0){
                a = a|(a+1);
                diff--;
            }
        }
        return a;
    }
}
