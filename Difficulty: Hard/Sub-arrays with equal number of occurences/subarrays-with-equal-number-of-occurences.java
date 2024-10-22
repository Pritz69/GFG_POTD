//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;
import java.util.HashMap;


// } Driver Code Ends
// User function Template for Java

class Solution {

    static int sameOccurrence(int arr[], int x, int y) {
        int n=arr.length;
        HashMap<Integer,Integer>map = new HashMap<>();
        
        for(int i=0;i<n;i++){
            if(arr[i]==x) arr[i]=1;
            else if(arr[i]==y) arr[i]=-1;
            else arr[i]=0;
        }
        int ans=0;
        int sum=0;
        map.put(0,1);
        for(int i=0;i<n;i++){
            sum+=arr[i];
            
            if(!map.containsKey(sum)){
                map.put(sum,1);
            }else{
                ans+=map.get(sum);
                map.put(sum,map.get(sum)+1);
                
            }
        }
        return ans;
    }
}

//{ Driver Code Starts.
public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
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

            int x = Integer.parseInt(br.readLine());
            int y = Integer.parseInt(br.readLine());
            // Create Solution object and find closest sum
            Solution ob = new Solution();
            int ans = ob.sameOccurrence(arr, x, y);
            System.out.println(ans);
        }
    }
}

// } Driver Code Ends