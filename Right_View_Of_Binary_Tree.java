//User function Template for Java


/*Complete The Function Provided
Given Below is The Node Of Tree
class Node
{
    int data;
    Node left, right;
    public Node(int data)
    {
        this.data = data;
         left = right = null;
    }
}*/


class Solution{
    //Function to return list containing elements of right view of binary tree.
    ArrayList<Integer> rightView(Node node) {
        //add code here.
        ArrayList<Integer> ans=new ArrayList<Integer>();
        Queue<Node> q=new LinkedList<Node>();
        q.offer(node);
        while (!q.isEmpty())
        {
            int s=q.size();
            for(int i=0;i<s;i++)
            {
                Node c=q.poll();
                if (i==s-1)
                {
                    ans.add(c.data);
                }
                if (c.left !=null)
                {
                    q.offer(c.left);
                }
                if (c.right !=null)
                {
                    q.offer(c.right);
                }
            }
        }
        return ans;
    }
}
