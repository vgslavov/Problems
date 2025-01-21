#include <cstddef>
#include <iostream>

// number: 701
// section:
// difficulty: medium
// tags: tree, bst, binary tree

// constraints
// The number of nodes in the tree will be in the range [0, 10^4].
// -10^8 <= Node.val <= 10^8
// All the values Node.val are unique.
// -10^8 <= val <= 10^8
// It's guaranteed that val does not exist in the original BST.

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
// run-time: O(log n)
// space: O(1)
TreeNode* insertIntoBST(TreeNode* root, int val)
{
    // insert leaf
    if (root == nullptr) {
        return new TreeNode(val);
    // insert left leaf
    } else if (root->left == nullptr && val < root->val) {
        root->left = new TreeNode(val);
        return root;
    // insert right leaf
    } else if (root->right == nullptr && root->val < val) {
        root->right = new TreeNode(val);
        return root;
    // go left
    } else if (val < root->val) {
        insertIntoBST(root->left, val);
        return root;
    // go right
    } else if (root->val < val) {
        insertIntoBST(root->right, val);
        return root;
    // duplicate found
    } else {
        std::cout << "duplicate value found: " << root->val << std::endl;
    }

    return root;
}
