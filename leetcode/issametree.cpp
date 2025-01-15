#include <cstddef>

// number: 100
// section: binary tree general
// difficulty: easy
// tags: tree, dfs, bfs, binary tree, top 150
//
// constraints
// The number of nodes in both trees is in the range [0, 100].
// -10^4 <= Node.val <= 10^4

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
bool isSameTree(TreeNode* p, TreeNode* q)
{
    if (!p && !q) {
        return true;
    } else if (!p || !q) {
        return false;
    }

    if (p->val != q->val) {
        return false;
    }

    if (!isSameTree(p->left, q->left)) {
        return false;
    }

    if (!isSameTree(p->right, q->right)) {
        return false;
    }

    return true;
}

// TODO: add unit tests
