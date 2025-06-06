#include <vector>

// number: 94
// title: Binary Tree Inorder Traversal
// url: https://leetcode.com/problems/binary-tree-inorder-traversal/
// difficulty: easy
// tags: stack, tree, dfs, binary tree

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
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

std::vector<int> nodes;

void dfs(TreeNode* node)
{
    if (!node) {
        return;
    }

    dfs(node->left);
    nodes.push_back(node->val);
    dfs(node->right);
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
std::vector<int> inorderTraversal(TreeNode* root)
{
    dfs(root);
    return nodes;
}

// TODO: add unit tests