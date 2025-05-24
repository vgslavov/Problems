#include <cstddef>

// number: 129
// title: Sum Root to Leaf Numbers
// url: https://leetcode.com/problems/sum-root-to-leaf-numbers/
// section: binary tree
// difficulty: medium
// tags: tree, dfs, binary tree, top 150

// contraints
// The number of nodes in the tree is in the range [1, 1000].
// 0 <= Node.val <= 9
// The depth of the tree will not exceed 10.

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

void dfs(TreeNode* root, int rootToLeaf, int& total)
{
    if (!root) {
        return;
    } else if (!root->left && !root->right) {
        total += rootToLeaf * 10 + root->val;
        return;
    }

    rootToLeaf = rootToLeaf * 10 + root->val;
    dfs(root->left, rootToLeaf, total);
    dfs(root->right, rootToLeaf, total);
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
int sumNumbers(TreeNode* root)
{
    int total = 0;
    dfs(root, 0, total);
    return total;
}
