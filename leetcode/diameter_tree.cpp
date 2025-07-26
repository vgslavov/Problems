#include <algorithm>

// number: 543
// title: Diameter of Binary Tree
// url: https://leetcode.com/problems/diameter-of-binary-tree/
// difficulty: easy
// tags: tree, dfs, binary tree, meta, grind 75

// constraints
// The number of nodes in the tree is in the range [1, 10^4].
// -100 <= Node.val <= 100

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int diameter = 0;

int dfs(TreeNode* node)
{
    // base case
    if (!node) {
        return 0;
    }

    int left = dfs(node->left);
    int right = dfs(node->right);

    diameter = std::max(diameter, left+right);

    return std::max(left, right)+1;
}

// solution: recursive dfs
// complexity:
// run-time: O(n)
// space: O(n)
int diameterOfBinaryTree(TreeNode* root)
{
    dfs(root);
    return diameter;
}

// TODO: add unit tests