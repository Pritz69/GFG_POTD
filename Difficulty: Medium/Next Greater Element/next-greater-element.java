//{ Driver Code Starts
import java.io.*;
import java.util.*;

class Geeks {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine()); // Number of test cases
        for (int g = 0; g < t; g++) {
            String[] str =
                (br.readLine()).trim().split(" "); // Reading input as a string array
            int arr[] = new int[str.length]; // Creating integer array from the input
            for (int i = 0; i < str.length; i++) {
                arr[i] = Integer.parseInt(str[i]);
            }

            // Getting the result from the Solution class
            ArrayList<Integer> result = new Solution().nextLargerElement(arr);

            // Printing the result in the required format
            if (result.isEmpty()) {
                System.out.println("[]");
            } else {
                for (int i = 0; i < result.size(); i++) {
                    if (i != 0) System.out.print(" ");
                    System.out.print(result.get(i));
                }
                System.out.println();
                System.out.println("~");
            }
        }
    }
}

// } Driver Code Ends

class Solution {

    public ArrayList<Integer> nextLargerElement(int[] arr) {
        // code here
        int size = arr.length;
        Stack<Integer> s= new Stack<>();
        ArrayList<Integer> result= new ArrayList<>();
        result.add(-1);
        s.push(arr[size-1]);

        for(int i=size-2;i>=0;i--) {

            while(!s.isEmpty() && s.peek()<=arr[i]) s.pop();
            if(s.isEmpty()) 
                result.add(-1);

            else 
                result.add(s.peek());

            s.push(arr[i]);

        }
        
        Collections.reverse(result);

        return result;
    }
}

