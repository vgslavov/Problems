#include <cstddef>

// number: 222
// title: Count Complete Tree Nodes
// url: https://leetcode.com/problems/count-complete-tree-nodes/
// section: binary tree general
// difficulty: easy
// tags: binary search, bit manipulation, tree, binary tree, top 150

// constraints
// The number of nodes in the tree is in the range [0, 5 * 10^4].
// 0 <= Node.val <= 5 * 10^4
// The tree is guaranteed to be complete.

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
int countNodes(TreeNode* root)
{
    if (root == nullptr) {
        return 0;
    }

    return countNodes(root->left) + countNodes(root->right) + 1;
}
