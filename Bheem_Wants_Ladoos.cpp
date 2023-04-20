class Solution{
    public:
    Node *king;                           
    unordered_map<Node *, Node *> parent; 
    int LevelOrder(int k)
    {
    int sum = 0;
    queue<Node *> q;
    q.push(king);
    unordered_map<Node *, bool> vis;
    vis[king] = true;
    int steps = 0;
    while (!q.empty())
    {
        int qsize = q.size();
        while (qsize--)
        {
            auto curr = q.front();
            q.pop();
            sum += curr->data;
            if (curr->left && !vis[curr->left])
            {
                vis[curr->left] = true;
                q.push(curr->left);
            }
            if (curr->right && !vis[curr->right])
            {
                vis[curr->right] = true;
                q.push(curr->right);
            }
            if (parent[curr] && !vis[parent[curr]])
            {
                vis[parent[curr]] = true;
                q.push(parent[curr]);
            }
        }
        if (steps == k)
            break;
        steps++;
    }
    return sum;
    }
// Find the home and make the parent map
void MakeParent(Node *root, int home)
{
    queue<Node *> q;
    q.push(root);
    parent[root] = NULL;
    while (!q.empty())
    {
        auto curr = q.front();
        q.pop();
        // Searching the home
        if (curr->data == home)
        {
            king = curr;
        }
        if (curr->left)
        {
            q.push(curr->left);
            parent[curr->left] = curr;
        }
        if (curr->right)
        {
            q.push(curr->right);
            parent[curr->right] = curr;
        }
    }
}
int ladoos(Node *root, int home, int k)
{
    MakeParent(root, home);
    return LevelOrder(k);
}
};
