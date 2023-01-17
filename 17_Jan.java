class Solution {
    int max_gcd = -1;
    int ans = -1;
    int gcd(int a, int b)
    {
        if(a==0) return b;
        return gcd(b%a, a);
    }
    int rec(Node root)
    {
        if(root==null) return -1;
        
        int l = rec(root.left);
        int r = rec(root.right);
        
        if(l!=-1 && r!=-1)
        {
            int gcd = gcd(l, r);
            if(max_gcd < gcd)
            {
                max_gcd = gcd;
                ans = root.data;
            }
            else if(max_gcd == gcd)
            {
                if(ans<root.data)
                {
                    ans = root.data;
                }
            }
        }
        return root.data;
    }
    int maxGCD(Node root)
    {
        ans = 0;
        
        rec(root);
        
        return ans;
    }
}
