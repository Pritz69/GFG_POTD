
//User function Template for Java

/*Complete the function below
Node is as follows:
class Node{
	int data;
	Node left,right;
	Node(int d){
		data=d;
		left=right=null;
	}
}
*/
class Solution
{
    // returns the inorder successor of the Node x in BST (rooted at 'root')
	public Node inorderSuccessor(Node root,Node x)
         {
          //add code here.
          Node suc=null;
          while (root != null)
          {
              if (root.data > x.data)
              {
                  suc=root;
                  root=root.left;
              }
              else
              {
                  root=root.right;
              }
          }
          return suc;
         }
}
