//{ Driver Code Starts
// Initial Template for Java
import java.util.*;


// } Driver Code Ends

// User function Template for Java
class Solution {
    public int findTarget(int arr[], int target) {
        // code here
        int N = arr.length;
        
        int lo = 0, hi = N-1;
        while(lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if(arr[mid] == target) return mid;
            else if(arr[mid] > target) {
                if((mid - 1) >= lo) {
                    if(arr[mid-1] == target) return mid-1;
                }
                if((mid + 1) <= hi) {
                    if(arr[mid+1] == target) return mid + 1;
                }
                hi = mid-1;
            }
            else {
                if((mid - 1) >= lo) {
                    if(arr[mid-1] == target) return mid-1;
                }
                if((mid + 1) <= hi) {
                    if(arr[mid+1] == target) return mid + 1;
                }
                lo = mid + 1;
                
            }
            
        }
        return -1;
    }
}


//{ Driver Code Starts.

public class GFG {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        while (t-- > 0) {
            String temp[] = sc.nextLine().trim().split(" ");
            int n = temp.length;
            int arr[] = new int[n];
            int target = sc.nextInt();
            if (sc.hasNextLine()) sc.nextLine();
            for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(temp[i]);
            Solution sln = new Solution();
            int ans = sln.findTarget(arr, target);
            System.out.println(ans);
            System.out.println("~");
        }
    }
}
// } Driver Code Ends