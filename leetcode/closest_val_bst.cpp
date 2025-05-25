#include <algorithm>
#include <cstddef>
#include <tuple>

// number: 270
// title: Closest Binary Search Tree Value
// url: https://leetcode.com/problems/closest-binary-search-tree-value/
// section: assessment
// difficulty: easy
// tags: binary search, tree, dfs, bst, bineary tree, meta

// constraints
// The number of nodes in the tree is in the range [1, 10^4].
// 0 <= Node.val <= 10^9
// -10^9 <= target <= 10^9

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

std::tuple<double, int> minDiff(TreeNode* root, double target) {
    // empty
    if (root == nullptr) {
        return std::tuple<double,int>(std::numeric_limits<int>::max(),0);
    // leaf
    } else if (root->left == nullptr && root->right == nullptr) {
        return std::tuple<double,int>(std::abs(root->val - target), root->val);
    }

    std::tuple<double,int> diff;

    // use BST properties!
    if (target == root->val) {
        return std::tuple<double,int>(0, root->val);
    } else if (target < root->val) {
        diff = minDiff(root->left, target);
    } else {
        diff = minDiff(root->right, target);
    }

    return std::min(
            std::tuple<double,int>(std::abs(root->val - target), root->val),
            diff);
}

// solution: recursive dfs
// complexity
// run-time: O(log n)
// space: O(n)
int closestValue(TreeNode* root, double target)
{
    return std::get<1>(minDiff(root, target));
}

// TODO: add unit tests
