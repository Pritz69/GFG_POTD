/*
class Node{
    int data;
    Node left;
    Node right;
    Node(int data){
        this.data = data;
        left=null;
        right=null;
    }
}

*/
class Solution {
    public boolean isSymmetric(Node root) {
        // Code here
        if(root == null) return true;
        return findsym(root.left,root.right);
    }
    
    private boolean findsym(Node p,Node q){
        
        if(p == null || q == null){
            return p == q;
        }
        
         if(p.data == q.data &&  findsym(p.left,q.right) && findsym(p.right,q.left)){
            return true;
        }
        
        return false;
    }
}