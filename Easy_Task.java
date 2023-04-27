//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    
	public static void main (String[] args) throws Exception{
        
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
                
        int t=Integer.parseInt(in.readLine());
        while(t-- > 0){
            int n=Integer.parseInt(in.readLine().trim());
            String s=in.readLine().trim();
            int q=Integer.parseInt(in.readLine().trim());
            query a[]=new query[q];
            for(int i=0;i<q;i++){
                String str=in.readLine().trim();
                String st[]=str.split(" ");
                if(st[0].trim().equals("1")){
                    a[i]=new query("1",st[1],st[2],"");
                }else{
                    a[i]=new query("2",st[1],st[2],st[3]);
                }
            }
            Solution ob=new Solution();
            ArrayList<Character> ans=ob.easyTask(n,s,q,a);
            for(char ch:ans){
                out.print(ch+" ");
            }out.println();
        }
        out.close();
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution 
{
    public static ArrayList<Character> easyTask(int n,String s,int q,query queries[])
    {
        ArrayList<Character> list=new ArrayList<>();
        for(int i=0;i<q;i++)
        {
            if(queries[i].type=="1")
            {
                s=getType1(s,Integer.parseInt(queries[i].a),queries[i].b.charAt(0));
            }
            else
            {
                list.add(getType2(s,Integer.parseInt(queries[i].a),Integer.parseInt(queries[i].b),Integer.parseInt(queries[i].c)));
            }
        }
        return list;
    }
    public static char getType2(String s,int left,int right,int k){
        int[] freq=new int[26];
        for(int i=left;i<=right;i++)
        {
            freq[(int)(s.charAt(i))-(int)'a']++;
        }
        int count=0;
        for(int i=25;i>=0;i--)
        {
            while(count<k && freq[i]>0)
            {
                count++;
                freq[i]--;
            }
            if(count==k){
                return (char)((int)'a'+i);
            }
        }
        return 'a';
    }
    public static String getType1(String s,int ind,char c){
        return s.substring(0,ind)+c+s.substring(ind+1);
    }
}
/*In case the query is of type 1.
type=1
c=null
*/

/*In case the query is of type 2.
type=2
c=k
*/

class query
{
    String type;
    String a;
    String b;
    String c;
    public query(String type,String a,String b,String c)
    {
        this.type=type;
        this.a=a;
        this.b=b;
        this.c=c;
    }
}
