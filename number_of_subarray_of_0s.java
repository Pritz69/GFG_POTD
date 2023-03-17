class Solution{
	long no_of_subarrays(int N, int [] arr) {
		//Write your code here
		long ans = 0, count = 0;
        for(int i = 0; i < N; i++){
           if(arr[i] == 0){
               count++;
               ans += count;
           }else{
               count = 0;
           }
        }
        return ans;
	}
}
