class Solution
{
    //Function to find a continuous sub-array which adds up to a given number.
    static ArrayList<Integer> subarraySum(int[] arr, int n, int s) 
    {
        // Your code here
        int sm=0;
        int l=0;
        int r=0;
        if(s==0)
        {
            ArrayList<Integer> ans=new ArrayList<>();
            ans.add(-1);
            return ans;
        }
        while(r<n)
        {
            if(sm<s)
            {
                sm+=arr[r];
            }
            if(sm>s)
            {
                while(sm>s)
                {
                    sm-=arr[l];
                    l+=1;
                }
            }
            if(sm==s)
            {
                ArrayList<Integer> ans=new ArrayList<>();
                ans.add(l+1);
                ans.add(r+1);
                return ans;
            }
            r +=1;
        }
        ArrayList<Integer> ans=new ArrayList<>();
        ans.add(-1);
        return ans;
    }
}
