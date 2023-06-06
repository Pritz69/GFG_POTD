//Function to check whether a Binary Tree is BST or not.
public static void findPreSuc(Node root, int key)
{
   if (root == null) {
        return;
    }
    
    if (root.data > key) {
        if (suc == null) {
            suc = root;
        } else if (suc != null && suc.data > root.data) {
            suc = root;
        } 
    }
    
    if (root.data < key) {
        if(pre == null) {
            pre = root;
        } else if (pre != null && pre.data < root.data) {
            pre = root;
        }
    }
    
    findPreSuc(root.left, key);
    findPreSuc(root.right, key);
    
}
