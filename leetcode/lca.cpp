#include <cstddef>

// number: 236
// title: Lowest Common Ancestor of a Binary Tree
// url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
// section: binary tree
// difficulty: medium
// tags: tree, dfs, binary tree, top 150

// constraints
// The number of nodes in the tree is in the range [2, 105].
// -109 <= Node.val <= 109
// All Node.val are unique.
// p != q
// p and q will exist in the tree.

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q)
{
    // empty tree
    if (root == nullptr) {
        return nullptr;
    }

    // 1) p or q is root, root is LCA
    if (root == p || root == q) {
        return root;
    }

    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);

    // 2) p and q in different subtrees, root is LCA
    if (left != nullptr && right != nullptr) {
        return root;
    }

    // 3) p and q in same subtree
    if (left != nullptr) {
        return left;
    }

    return right;
}

// TODO: add unit tests
