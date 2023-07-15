class Solution
{
    //Function to delete middle element of a stack.
    public void solve(Stack<Integer>s,int k)
    {
        if(k==0)
        {
            s.pop();
            return ;
        }
        int v=s.peek();
        s.pop();
        solve(s,k-1);
        s.push(v);
    }
    public void deleteMid(Stack<Integer>s,int sizeOfStack){
        // code here
        int k=sizeOfStack/2;
        solve(s,k);
    } 
}
