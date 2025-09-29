#include <cstddef>
#include <limits>

// tags: dfs, tree, bst

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

bool dfs(TreeNode* node, int left, int right)
{
    if (!node) {
        return;
    }

    // value has to be b/w left & right to be valid
    if (node->val > right || node->val < left) {
        return false;
    }

    // change search range: left to current & current to right
    return dfs(node->left, left, node->val) &&
           dfs(node->right, node->val, right);
}

// solution: recursive dfs
// complexity:
// run-time: O(n)
// space: O(n)
bool validBST(TreeNode* root)
{
    return dfs(
        root,
        std::numeric_limits<int>::min(),
        std::numeric_limits<int>::max());
}