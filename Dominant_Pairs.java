class Solution {
    public static int dominantPairs(int n, int[] arr) {
       
        int i=0,j=n/2;
        Arrays.sort(arr,0,j);
        Arrays.sort(arr,j,n);
        int count =0;
        
        while(i<n/2 && j<n){
            if(arr[i]>=5*arr[j]){
                count+=n/2-i;
                j++;
            }else{
                i++;
            }
        }
        return count;
    }
}
