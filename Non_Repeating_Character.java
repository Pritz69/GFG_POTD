class Solution
{
    //Function to find the first non-repeating character in a string.
    static char nonrepeatingCharacter(String S)
    {
        //Your code here
        HashMap<Character,Integer> h=new HashMap<Character,Integer>();
        for( int i=0;i< S.length();i++)
        {
            char x=S.charAt(i);
            h.put(x, h.getOrDefault(x,0)+1);
        }
        for( int i=0;i< S.length();i++)
        {
            char x=S.charAt(i);
            if (h.get(x)==1)
            {
                return x;
            }
        }
        return '$';
    }
}
