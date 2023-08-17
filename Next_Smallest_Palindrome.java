

// User function Template for Java

class Solution {

    Vector<Integer> generateNextPalindrome(int num[], int n) {
        // code here
        Vector<Integer> ans=new Vector<>();
        boolean change=true;
        for(int i=0;i<n/2;i++)
        {
            if(num[i]<num[n-i-1])
            {
                change=true;            
            }
            else if (num[i] > num[n - i - 1])   // 9 4 1 8 7 9 7 8 1 4 9
            {
                change = false;
            }
            num[n-i-1]=num[i];
        }
        for(int i=0;i<n;i++)                
        {
            ans.add(num[i]);
        }
        int ind=n/2;
        while(change && ind<n)
        {
            if(ans.get(ind)==9)
            {
                ans.set(ind,0);
                ans.set(n-ind-1,0);
            }
            else
            {
                int v=ans.get(ind);
                ans.set(ind,v+1);
                ans.set(n-ind-1,v+1);
                change=false;
            }
            ind ++;
        }
        if(change)
        {
            ans.set(0,1);
            ans.add(1);
        }
        return ans;
    }
}
