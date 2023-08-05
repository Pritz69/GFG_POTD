

//User function Template for Java


class Solution
{
    public void permute(String s,List<String> ans,StringBuilder temp,int freq[])
    {
        if(temp.length()==s.length())
        {
            ans.add(temp.toString());
            return ;
        }
        for(int i=0;i<s.length();i++)
        {
            if(freq[i]==0)
            {
                freq[i]=1;
                temp.append(s.charAt(i));
                permute(s,ans,temp,freq);
                temp.deleteCharAt(temp.length()-1);
                freq[i]=0;
            }
        }
    }
    public ArrayList<String> permutation(String s)
    {
        //Your code here
        ArrayList<String> ans=new ArrayList<>();
        int freq[]=new int[s.length()];
        StringBuilder sb=new StringBuilder();
        permute(s,ans,sb,freq);
        Collections.sort(ans);
        return ans;
    }
	   
}
