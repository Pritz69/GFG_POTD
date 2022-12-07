class Solution {

  public:

    int ans = -1;

    void inorder(Node * root , int &K){

        if(!root){

            return;

        }

        inorder(root->left,K);

        K--;

        if(K==0){

            ans = root->data;

            return;

        }

        inorder(root->right,K);
    }

    int KthSmallestElement(Node *root, int K) {

        inorder(root,K);

        return ans;

      }

};
