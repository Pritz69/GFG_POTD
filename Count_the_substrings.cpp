//User function Template for C++
class Solution
{
    public:
    int countSubstring(string S)
    {
        // code here
        int ans=0;
        for(int i=0;i<S.size(); i++)
        {
            int low=0;
            int upp=0;
            for(int j=i; j<S.size(); j++)
            {
                if(S[j]>='a' and S[j]<='z')
                {
                    low++;
                }
                if(S[j]>='A' and S[j]<='Z')
                {
                    upp++;
                }
                if(low==upp)
                {
                    ans++;
                }
            }
            
        }
        
        return ans;
    }
};
