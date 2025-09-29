#include <algorithm>
#include <cstddef>

// tags: dfs, tree

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
TreeNode* invertBinaryTree(TreeNode* node)
{
    if (!node) {
        return nullptr;
    }

    std::swap(node->left, node->right);

    invertBinaryTree(node->left);
    invertBinaryTree(node->right);

    return node;
}