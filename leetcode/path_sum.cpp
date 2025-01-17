// number: 112
// section: binary tree general
// difficulty: easy
// tags: tree, dfs, bfs, binary tree, top 150

// constraints
// The number of nodes in the tree is in the range [0, 5000].
// -1000 <= Node.val <= 1000
// -1000 <= targetSum <= 1000

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
    : val(x), left(left), right(right) {}
};

int dfs(TreeNode* root, int targetSum, int currSum)
{
    if (!root) {
        return false;
    // leaf
    } else if (!root->left && !root->right) {
        return targetSum == currSum + root->val;
    }

    currSum += root->val;

    return dfs(root->left, targetSum, currSum) ||
           dfs(root->right, targetSum, currSum);
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
bool hasPathSum(TreeNode* root, int targetSum)
{
    return dfs(root, targetSum, 0);
}
