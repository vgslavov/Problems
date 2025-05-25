#include <algorithm>
#include <cstddef>

// number: 226
// title: Invert Binary Tree
// url: https://leetcode.com/problems/invert-binary-tree/
// section: binary tree general
// difficulty: easy
// tags: tree, dfs, bfs, binary tree, top 150
//
// constraints
// The number of nodes in the tree is in the range [0, 100].
// -100 <= Node.val <= 100

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

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
TreeNode* invertTree(TreeNode* root)
{
    if (!root) {
        return nullptr;
    }

    std::swap(root->left, root->right);
    invertTree(root->left);
    invertTree(root->right);

    return root;
}

// TODO: add unit tests
