//{ Driver Code Starts
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = Integer.parseInt(scanner.nextLine()); // Read number of test cases

        // Loop through each test case
        while (t-- > 0) {
            String input = scanner.nextLine();
            String[] inputArr = input.split(" ");
            List<Integer> arr = new ArrayList<>();

            // Convert input to list of integers
            for (String str : inputArr) {
                arr.add(Integer.parseInt(str));
            }

            Solution ob = new Solution();
            boolean ans = ob.checkSorted(arr);

            // Output result
            if (ans)
                System.out.println("true");
            else
                System.out.println("false");
        }

        scanner.close();
    }
}

// } Driver Code Ends


class Solution {

    public boolean checkSorted(List<Integer> arr) {
        int wrongPos=0;
        int n=arr.size();
        for(int i=0;i<n;i++)
            if(arr.get(i)!=i+1) wrongPos++;
        if(wrongPos==3 || wrongPos==0) return true;
        if(wrongPos==1||wrongPos==2||wrongPos>4) return false;
        swapOnce(n,arr);
        swapOnce(n,arr);
        for(int i=0;i<n;i++)
            if(arr.get(i)!=i+1) return false;
        return true;
    }
    public void swapOnce(int size,List<Integer> arr){
        for(int i=0;i<size;i++){
            if(arr.get(i)!=i+1){
                for(int j=i+1;j<size;j++){
                    if(arr.get(j)==i+1){
                        Collections.swap(arr,i,j);
                        return;
                    }
                }
            }
        }
    }
}