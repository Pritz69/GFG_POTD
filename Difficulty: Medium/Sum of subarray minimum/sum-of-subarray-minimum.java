class Solution {
    public int sumSubMins(int[] arr) {
        int arrsum =0;
        
       
        for(int i =0;i<arr.length;i++){
            int minv = Integer.MAX_VALUE;
            for(int j = i;j<arr.length;j++){
                minv = Math.min(minv,arr[j]);
                arrsum += minv;
                
            }
           
        }
        
        return arrsum;
        // code here
        
    }
}