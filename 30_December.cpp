
class Solution
{
    public:
    bool solve(Node* root, int& c)
    {
        if(root==NULL)
            return true;
        bool lf = solve(root->left, c);
        bool rt = solve(root->right, c);
        if (lf == false || rt ==false)
        {
            return false;
        }
        if (root->left && root->data != root->left->data)
        {
            return false;
        }
        if (root->right && root->data != root->right->data)
        {
            return false;
        }
        c++;
        return true;
    }
    int singlevalued(Node *root){
        //code here
        int c = 0;
        solve(root, c);
        return c;
    }
};
