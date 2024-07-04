//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) throws IOException{
	    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	    StringTokenizer st=new StringTokenizer(br.readLine());
	    int t=Integer.parseInt(st.nextToken());
	    while(t-->0){
	        String s=br.readLine();
	        
	        Solution obj = new Solution();
	        
	        System.out.println(obj.findSum(s));
	    }
		
	}
}

// } Driver Code Ends




class Solution
{
    //Function to calculate sum of all numbers present in a string.
    public static long findSum(String str)
    {
        // your code here
        int s=0;
        int c=0;
        for(int i=0;i<str.length();i++)
        {
            if ((65 <= (int)(str.charAt(i)) && (int)(str.charAt(i))<= 90) || (97 <= (int)(str.charAt(i)) && (int)(str.charAt(i)) <=122))
            {
                s +=c;
                c=0;
            }
            else
            {
                String sa=str.substring(i,i+1);
                c=c*10 + Integer.valueOf(sa);
            }
        }
        s +=c;
        return s;
    }
    
}