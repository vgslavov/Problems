#include <algorithm>

// number: 104
// title: Maximum Depth of Binary Tree
// url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
// section: binary tree general
// difficulty: easy
// tags: tree, dfs, bfs, binary tree, top 150, leetcode 75

// constraints
// The number of nodes in the tree is in the range [0, 10^4].
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
int maxDepth(TreeNode* root)
{
    if (!root) {
        return 0;
    }

    return std::max(maxDepth(root->left), maxDepth(root->right)) + 1;
}
