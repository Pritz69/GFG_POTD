
//User function Template for Java


/*
// A Binary Tree node
class Node
{
    int data;
    Node left, right;

    Node(int item)
    {
        data = item;
        left = right = null;
    }
}
*/

class Spiral
{
    //Function to return a list containing the level order 
    //traversal in spiral form.	
    ArrayList<Integer> findSpiral(Node root) 
    {
        // Your code here
        ArrayList<Integer> ans = new ArrayList<Integer>();
        Queue<Node> q=new LinkedList<>();
        q.offer(root);
        int c=0;
        while (!q.isEmpty())
        {
            int s=q.size();
            if (c%2==1)
            {
                for(int i=0;i<s;i++)
                {
                        Node n=q.poll();
                        ans.add(n.data);
                        if (n.left !=null)
                        {
                            q.offer(n.left);
                        }
                        if (n.right !=null)
                        {
                            q.offer(n.right);
                        }
                }
            }
            if(c%2==0)
            {
                Stack<Integer> st= new Stack<>();
                for(int i=0;i<s;i++)
                {
                        Node n=q.poll();
                        st.push(n.data);
                        if (n.left !=null)
                        {
                            q.offer(n.left);
                        }
                        if (n.right !=null)
                        {
                            q.offer(n.right);
                        }
                }
                while(!st.isEmpty())
                {
                    ans.add(st.pop());
                }
            }
            c +=1;
        }
        return ans;
    }
}
