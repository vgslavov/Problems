#include <cstddef>
#include <vector>

// number: 230
// title: Kth Smallest Element in a BST
// url: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
// section: binary search tree
// difficulty: medium
// tags: tree, dfs, bst, binary tree, top 150

// constraints
// The number of nodes in the tree is n.
// 1 <= k <= n <= 10^4
// 0 <= Node.val <= 10^4

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

// complexity
// run-time: O(n)
// space: O(n)
void dfs(TreeNode* root, std::vector<int>& v)
{
    if (!root) {
        return;
    }

    dfs(root->left, v);
    v.push_back(root->val);
    dfs(root->right, v);
}

// solution: recursive in-order dfs
// complexity
// run-time: O(n)
// space: O(n)
int kthSmallest(TreeNode* root, int k)
{
    std::vector<int> sorted;
    dfs(root, sorted);

    return sorted[k-1];
}

// TODO: solve in O(log n) & add unit tests
