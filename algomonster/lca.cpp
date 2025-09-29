#include <cstddef>

// tags: dfs, binary tree

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// solution: recursive dfs
// complexity:
// run-time: O(n)
// space: O(n)
TreeNode* lca(TreeNode* root, TreeNode* node1, TreeNode* node2)
{
    if (!root) {
        return nullptr;
    }

    // 1. p or q is root
    if (root == node1 || root == node2) {
        return root;
    }

    // 2. p is in left subtree, q is right subtree
    TreeNode* left = lca(root->left, node1, node2);
    TreeNode* right = lca(root->right, node1, node2);

    if (left && right) {
        return root;
    }

    // 3. p & q in same subtree
    if (left) {
        return left;
    }

    return right;
}