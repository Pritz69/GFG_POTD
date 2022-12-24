class Solution {
    long wineSelling(int Arr[],int N){
        // code here
        long sum = 0;
        long ans = 0;
        for(int i=0; i<N; i++)
        {
            ans+=Math.abs(sum);  
            sum+=Arr[i]; 
        }
        return ans;
    }
}
