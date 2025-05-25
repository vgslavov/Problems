#include <cstddef>
#include <map>
#include <vector>

// number: 106
// title: Construct Binary Tree from Inorder and Postorder Traversal
// url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
// section: binary tree
// difficulty: medium
// tags: array, hash table, divide & conquer, tree, binary tree

// constraints
// 1 <= inorder.length <= 3000
// postorder.length == inorder.length
// -3000 <= inorder[i], postorder[i] <= 3000
// inorder and postorder consist of unique values.
// Each value of postorder also appears in inorder.
// inorder is guaranteed to be the inorder traversal of the tree.
// postorder is guaranteed to be the postorder traversal of the tree.

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

TreeNode* array2Tree(std::vector<int>& postorder, int left, int right)
{
    if (left > right) {
        return nullptr;
    }

    // root is last!
    int rootVal = postorder.back();
    // remove it!
    postorder.pop_back();

    // create node
    TreeNode* root = new TreeNode(rootVal);

    int root_i = value2index[rootVal];

    // split inorder tree at root
    // do right first!
    root->right = array2Tree(postorder, root_i+1, right);
    root->left = array2Tree(postorder, left, root_i-1);

    return root;
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
TreeNode* buildTree2(
        const std::vector<int>& inorder,
        std::vector<int>& postorder)
{
    // indices of all value in inorder
    for (size_t i = 0; i != inorder.size(); ++i) {
        value2index[inorder[i]] = i;
    }

    return array2Tree(postorder, 0, postorder.size()-1);
}
