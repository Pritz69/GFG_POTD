

//User function Template for Java


class Solution {

    public static int maxOnes(int a[], int n) {
        // Your code goes here
        int o=0;
        for(int x:a)
        {
            if (x==1)
            {
                o +=1;
            }
        }
        int z=0; 
        int mx=0;
        for(int i=0;i<n;i++)
        {
            if(a[i]==0)
            {
                z +=1;
            }
            else
            {
                if(z>=1)
                {
                    z -=1;
                }
            }
            mx=Math.max(mx,z);
        }
        return mx+o;
    }
}
