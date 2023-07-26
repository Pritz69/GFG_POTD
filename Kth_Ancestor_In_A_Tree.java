
//User function Template for Java

/*
Structure of Node class is:

class Node {
    int data;
    Node left, right;
    
    public Node(int data){
        this.data = data;
    }
}
*/

class Solution
{
    public int kthAncestor(Node root, int k, int node)
    {
        //Write your code here
        int n=0;
        Queue<Node> q=new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty())
        {
            Node c=q.poll();
            if (c !=null)
            {
                n=Math.max(n,c.data);
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
        int a[]=new int[n+1];
        a[root.data]=-1;
        Queue<Node> qu=new LinkedList<>();
        qu.offer(root);
        while (!qu.isEmpty())
        {
            Node c=qu.poll();
            if (c !=null)
            {
                if (c.left !=null)
                {
                    qu.offer(c.left);
                    a[c.left.data]=c.data;
                }
                if (c.right !=null)
                {
                    qu.offer(c.right);
                    a[c.right.data]=c.data;
                }
            }
        }
        int ans=-1;
        int ind=node;
        while (ind != -1)
        {
            ans=a[ind];
            ind=ans;
            k -=1;
            if (k==0)
            {
                return ans;
            }
        }
        return -1;
    }
}
