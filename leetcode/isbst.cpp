#include <limits>

// number: 98
// section: binary search tree
// difficulty: medium
// tags: tree, dfs, bfs, binary tree, top 150, meta, sig

// constraints
// The number of nodes in the tree is in the range [1, 10^4].
// -2^31 <= Node.val <= 2^31 - 1

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

bool dfs(TreeNode* root, long long int start, long long int end) {
    if (!root) {
        return true;
    }

    if (start >= root->val || end <= root->val) {
        return false;
    }

    return dfs(root->left, start, root->val) &&
           dfs(root->right, root->val, end);
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
bool isBST(TreeNode* root)
{
    return dfs(root,
               std::numeric_limits<long long int>::min(),
               std::numeric_limits<long long int>::max());
}
