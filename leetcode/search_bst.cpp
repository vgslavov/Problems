#include <cstddef>

// number: 700
// section: recursion
// difficulty: easy
// tags: tree, bst, binary tree

// constraints
// The number of nodes in the tree is in the range [1, 5000].
// 1 <= Node.val <= 10^7
// root is a binary search tree.
// 1 <= val <= 10^7

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

// solution: dfs
// complexity
// run-time: O(log n)
// space: O(log n)
TreeNode* searchBST(TreeNode* root, int val)
{
    if (!root) {
        return nullptr;
    } else if (root->val == val) {
        return root;
    } else if (val > root->val) {
        return searchBST(root->right, val);
    } else {
        return searchBST(root->left, val);
    }

    return nullptr;
}
