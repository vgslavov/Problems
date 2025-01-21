#include <cstddef>

// number: 101
// section: binary tree general
// difficulty: easy
// tags: tree, dfs, bfs, binary tree, top 150

// constraints
// The number of nodes in the tree is in the range [1, 1000].
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

bool compare(TreeNode* p, TreeNode* q)
{
    if (!p && !q) {
        return true;
    } else if (!p or !q) {
        return false;
    }

    if (p->val != q->val) {
        return false;
    }

    if (!compare(p->left, q->right)) {
        return false;
    }

    if (!compare(p->right, q->left)) {
        return false;
    }

    return true;
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
bool isSymmetric(TreeNode* root)
{
    if (!root) {
        return false;
    }

    return compare(root->left, root->right);
}
