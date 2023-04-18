class Solution {
public:
    int f(Node *root, int &minlen, int &sum, int target, bool &flag, int &maxi, int &mini)
{
    if (root == NULL)
        return 0;

    // below subtrees sum,isbst,maxi,mini
    int leftsum = 0, rightsum = 0;
    bool leftflag = true, rightflag = true;
    int leftmaxi = -1e9, rightmaxi = -1e9;
    int leftmini = 1e9, rightmini = 1e9;

    int leftlen = f(root->left, minlen, leftsum, target, leftflag, leftmaxi, leftmini);
    int rightlen = f(root->right, minlen, rightsum, target, rightflag, rightmaxi, rightmini);

    sum = root->data + leftsum + rightsum;
    int currLen = leftlen + rightlen + 1;
    maxi = max(root->data, max(leftmaxi, rightmaxi));
    mini = min(root->data, min(leftmini, rightmini));
    flag = false;
    if (root->data > leftmaxi && root->data < rightmini && leftflag && rightflag)
    {
        flag = true; // current tree is also bst
    }
    if (currLen < minlen && sum == target && flag)
    {
        minlen = currLen;
    }
    return currLen;
}
int minSubtreeSumBST(int target, Node *root)
{
    int sum = 0, minlen = 1e9, maxi = -1e9, mini = 1e9;
    bool flag = true;
    f(root, minlen, sum, target, flag, maxi, mini);
    return minlen == 1e9 ? -1 : minlen;
}
};
