class Solution {

  public:

    int solve(Node* root,int &ans){

        if(root==NULL){

            return 0;

        }

        int left=solve(root->left,ans);

        int right=solve(root->right,ans);

        int curr=left+root->data+right;

        ans=max(ans,curr);

        return curr;

    }

    int findLargestSubtreeSum(Node* root)

    {

        //Write your code here

        int ans=INT_MIN;

        solve(root,ans);

        return ans;

    }

};
