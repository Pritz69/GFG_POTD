//{ Driver Code Starts
import java.util.*;

class Count
{
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int m = sc.nextInt();
            int n = sc.nextInt();
            
            int arr1[] = new int[m];
            int arr2[] = new int[n];
            
            for(int i = 0; i < m; i++)
              arr1[i] = sc.nextInt();
              
            for(int i = 0; i < n; i++)
              arr2[i] = sc.nextInt();
              
            Solution gfg = new Solution();
            ArrayList<Integer> res = gfg.countEleLessThanOrEqual(arr1, arr2, m, n);
            for (int i = 0; i < res.size(); i++)
                System.out.print (res.get (i) + " ");
            System.out.println();
        }
        
    }
}
// } Driver Code Ends


// Complete the function given below
class Solution
{
    public static ArrayList<Integer> countEleLessThanOrEqual(int arr1[], int arr2[], int m, int n)
    {
       // add your code here
       Arrays.sort(arr2);
       ArrayList<Integer>a=new ArrayList<>();
       for(int i=0;i<m;i++)
       {
           int el=arr1[i];
           int l=0;
           int h=n-1;
           int ans=0;
           while(l<=h)
           {
               int mid=(l+h)/2;
               if(arr2[mid] > el)
               {
                   h=mid-1;
               }
               else
               {
                   ans=mid;
                   l=mid+1;
               }
           }
           a.add(l);
       }
       return a;
    }
}