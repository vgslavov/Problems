#include <algorithm>
#include <cstddef>

// tags: dfs, tree

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : val(val), left(nullptr), right(nullptr) {}
};

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(h) average, O(n) worst if tree skewed
int maxDepth(TreeNode* root)
{
    if (!root) {
        return 0;
    }

    return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
}

// solution: recursive dfs
// complexity
// run-time: O(n^2)
// space: O(h) average, O(n) worst if tree skewed
bool isBalanced(TreeNode* node)
{
    if (!node) {
        return true;
    }

    return std::abs(maxDepth(node->left)-maxDepth(node->right)) <= 1
            && isBalanced(node->left)
            && isBalanced(node->right);
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(h) average, O(n) worst if tree skewed
int treeHeight(TreeNode* node)
{
    // base case
    if (!node) {
        return 0;
    }

    int leftHeight = treeHeight(node->left);
    int rightHeight = treeHeight(node->right);

    if (leftHeight == -1 || rightHeight == -1) {
        return -1;
    } else if (std::abs(leftHeight-rightHeight) > 1) {
        return -1;
    } else {
        return 1 + std::max(leftHeight, rightHeight);
    }
}

// solution: AlgoMonster recursive dfs
// complexity
// run-time: O(n)
// space: O(h) average, O(n) worst if tree skewed
bool isBalanced2(TreeNode* node)
{
    return treeHeight(node) != -1;
}