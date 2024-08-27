//{ Driver Code Starts
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            String input = br.readLine();
            String[] inputs = input.split(" ");
            int[] arr = new int[inputs.length];

            for (int i = 0; i < inputs.length; i++) {
                arr[i] = Integer.parseInt(inputs[i]);
            }

            Solution ob = new Solution();
            System.out.println(ob.findMaxDiff(arr));
        }
    }
}

// } Driver Code Ends


class Solution {
    public int findMaxDiff(int[] arr) {
        int[] leftNSmaller = new int[arr.length];
        int[] rightNSmaller = new int[arr.length];
        //for loop for left smaller
        for(int i =0; i<arr.length;i++){
            if(i==0){
                leftNSmaller[i]=0;
            }
            for(int k=i-1;k>=0;k--){
                if(arr[k]<arr[i]){
                    leftNSmaller[i]=arr[k];
                    break;
                }
                else if(k==0){
                    leftNSmaller[i]=0;
                }
            }
        }
        for(int i =0; i<arr.length;i++){
            if(i==arr.length-1){
                 rightNSmaller[i]=0;
            }
            for(int k=i+1;k<arr.length;k++){
                if(arr[k]<arr[i]){
                    rightNSmaller[i]=arr[k];
                    break;
                }
                else if(k==arr.length-1){
                    rightNSmaller[i]=0;
                }
            }
        }
        int max = maxDiffFinder(leftNSmaller, rightNSmaller);
        return max;
        
    }
    public int maxDiffFinder(int[] left, int[] right){
        int max=0;
        for(int i =0;i<left.length;i++){
            int tempMax = Math.abs(left[i]-right[i]);
            if(tempMax>max){
                max=tempMax;
            }
        }
        return max;
    }
}
