#include <cstddef>

// number: 114
// section: binary tree general
// difficulty: medium
// tags: linked list, stack, tree, dfs, binary tree

// constraint
// The number of nodes in the tree is in the range [0, 2000].
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

TreeNode* dfs(TreeNode* root) {
    if (!root) {
        return nullptr;
    } else if (!root->left && !root->right) {
        return root;
    }

    TreeNode* left_tail = dfs(root->left);
    TreeNode* right_tail = dfs(root->right);

    if (left_tail) {
        left_tail->right = root->right;
        root->right = root->left;
        root->left = nullptr;
    }

    return right_tail ? right_tail : left_tail;
}

// solution: leetcode recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
void flatten(TreeNode* root)
{
    dfs(root);
}
