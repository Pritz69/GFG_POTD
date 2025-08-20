class Solution {
    
    static boolean f(int arr[], int x){
        int l=0;
        int h=arr.length-1;
          
        while(l<=h){
            int mid=(l+h)>>1;
            
            if(arr[mid]==x)return true;
            
            if(arr[l]<=arr[mid]){
                if(arr[l]<=x && x<=arr[mid]){
                    h=mid-1;
                }else {
                    l=mid+1;
                }
                
            }else {
                if(arr[mid]<=x && x<=arr[h]){
                    l=mid+1;
                }else {
                    h=mid-1;
                }
            }
        }
        
        return false;
    }
    
    
    public boolean searchMatrix(int[][] mat, int x) {
        int m=mat[0].length;
        for(int i=0;i<mat.length;i++){
            if(mat[i][0]<=x && x<=mat[i][m-1]){
                if(f(mat[i],x))return true;
            }else if(mat[i][0]>mat[i][m-1]){
                if(f(mat[i],x))return true;
            }
        }
        
        return false;
    }
}