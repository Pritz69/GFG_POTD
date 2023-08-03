

//User function Template for Java

class Solution
{ 
    static void insertatbottom(Stack<Integer> s,int k)
    {
        if(s.isEmpty())
        {
            s.push(k);
            return ;
        }
        int t=s.pop();
        insertatbottom(s,k);
        s.push(t);
    }
    static void reverse(Stack<Integer> s)
    {
        // add your code here
        if(s.isEmpty())
        {
            return ;
        }
        int temp=s.peek();
        s.pop();
        reverse(s);
        insertatbottom(s,temp);
    }
}
