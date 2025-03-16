//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            String line = br.readLine();
            String[] tokens = line.split(" ");

            // Create an ArrayList to store the integers
            ArrayList<Integer> array = new ArrayList<>();

            // Parse the tokens into integers and add to the array
            for (String token : tokens) {
                array.add(Integer.parseInt(token));
            }

            int[] arr = new int[array.size()];
            int idx = 0;
            for (int i : array) arr[idx++] = i;

            System.out.println(new Solution().minJumps(arr));
            System.out.println("~");
        }
    }
}

// } Driver Code Ends


class Solution {
    static int minJumps(int[] arr) {
        if (arr.length <= 1) return 0; // Already at the last index
        if (arr[0] == 0) return -1;   // Cannot move from the first index

        int maxReach = arr[0]; // Maximum index we can reach
        int steps = arr[0];    // Steps we can take before we need another jump
        int jumps = 1;         // We start with one jump (from index 0)

        for (int i = 1; i < arr.length; i++) {
            if (i == arr.length - 1) return jumps; // Reached last index

            maxReach = Math.max(maxReach, i + arr[i]); // Update max reach
            steps--; // Decrease steps since we move forward

            if (steps == 0) { // If no more steps left, we must jump
                jumps++; // Increase jump count
                if (i >= maxReach) return -1; // If maxReach is behind, we are stuck
                steps = maxReach - i; // Recalculate steps for the new jump
            }
        }

        return -1; // If we exit the loop, we never reached the last index
    }
}

