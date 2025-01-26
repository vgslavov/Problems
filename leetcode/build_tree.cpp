#include <cstddef>
#include <map>
#include <vector>

// number: 105
// section: binary tree general
// difficulty: medium
// tags: array, hash table, divide & conquer, tree, binary tree

// constraints
// 1 <= preorder.length <= 3000
// inorder.length == preorder.length
// -3000 <= preorder[i], inorder[i] <= 3000
// preorder and inorder consist of unique values.
// Each value of inorder also appears in preorder.
// preorder is guaranteed to be the preorder traversal of the tree.
// inorder is guaranteed to be the inorder traversal of the tree.

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

std::map<int, int> value2index;
int preorder_i = 0;

TreeNode* array2Tree(const std::vector<int>& preorder, int left, int right)
{
    if (left > right) {
        return nullptr;
    }

    // keep track of preorder index: it's the root of a subtree
    int rootVal = preorder[preorder_i];
    TreeNode* root = new TreeNode(rootVal);
    ++preorder_i;

    // find index of root in inorder
    int root_i = value2index[rootVal];

    // split left & right subtrees from inorder but exclude root
    root->left = array2Tree(preorder, left, root_i-1);
    root->right = array2Tree(preorder, root_i+1, right);

    return root;
}

// solution: leetcode recursive dfs
// run-time: O(n)
// space: O(n)
TreeNode* buildTree(
        const std::vector<int>& preorder,
        const std::vector<int>& inorder)
{
    // value to index map in inorder
    for (size_t i = 0; i != inorder.size(); ++i) {
        value2index[inorder[i]] = i;
    }

    return array2Tree(preorder, 0, inorder.size()-1);
}
