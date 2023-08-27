

//User function Template for Java


class Reverse
{
    // Complete the function
    // str: input string
    public static String reverseWord(String str)
    {
        // Reverse the string str
        StringBuilder sb = new StringBuilder(str);
        int l=0;
        int r=str.length()-1;
        while(l<=r)
        {
            char ch=sb.charAt(l);
            sb.setCharAt(l,sb.charAt(r));
            sb.setCharAt(r,ch);
            l+=1;
            r-=1;
        }
        return sb.toString();
    }
}
