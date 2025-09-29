#include <cstddef>

// tags: dfs, bst

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
int lcaOnBST(TreeNode* bst, int p, int q)
{
    // 1. p & q in right subtree
    if (p > bst->val && q > bst->val) {
        return lcaOnBST(bst->right, p, q);
    // 2. p & q in left subtree
    } else if (p < bst->val && q < bst->val) {
        return lcaOnBST(bst->left, p, q);
    // 3. p or q is root, check last!
    } else {
        return bst->val;
    }

    return 0;
}