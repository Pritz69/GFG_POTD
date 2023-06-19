
class Solution
{
 
    // arr: input array
    // n: size of array
    //Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    //with O(1) extra space.
    static void arrange(long arr[], int n)
    {
        // your code here
        for (int i=0;i<n;i++)
        {
            int x=(int)arr[i];
            long y=arr[x];
            arr[i]= x + (y%n)*n;
        }
        for (int i=0;i<n;i++)
        {
            arr[i] =arr[i]/n;
        }
    }
}
