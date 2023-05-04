//User function Template for Java
class Solution{
    public static int maxCoins(int n,int r[][])
    {
         Arrays.sort(r,new Comparator<int[]>(){
            public int compare(int first[],int second[]){
                if(first[0]==second[0])
                return first[1]-second[1];
                else
                return first[0]-second[0];
            }
        });
        
        int help[] = new int[n]; help[n-1]=r[n-1][2];
        for(int i=n-2; i>=0; i--)
        { 
            help[i] = Math.max(help[i+1], r[i][2]);
        }
        int ans=Integer.MIN_VALUE; int t=0;
        for(int i=0; i<n; i++)
        {
            int l=i+1; int h=n-1;
            int curr_ans= r[i][2];
            while(l<=h)
            {
                int m = (l+h)/2;
                if(r[m][0] >= r[i][1]) //its poss ans and need to search in lower range as well(as coins can be greater there)
                { 
                    curr_ans=Math.max(curr_ans, r[i][2] + help[m]); 
                    h=m-1; 
                }
                else l=m+1;
            }
            ans = Math.max(curr_ans, ans);
        }
       return ans;
    }
}
