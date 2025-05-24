#include <cstddef>
#include <vector>

// number: 108
// title: Convert Sorted Array to Binary Search Tree
// url: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
// section: divide & conquer
// difficulty: easy
// tags: array, divide & conquer, tree, bst, binary tree, top 150

// constraints
// 1 <= nums.length <= 10^4
// -10^4 <= nums[i] <= 10^4
// nums is sorted in a strictly increasing order.

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

TreeNode* dfs(const std::vector<int>& nums, int left, int right)
{
    if (left > right) {
        return nullptr;
    }

    // choose root as left middle
    int mid = (left+right) / 2;

    // pre-order traversal
    TreeNode* root = new TreeNode(nums[mid]);
    root->left = dfs(nums, left, mid-1);
    root->right = dfs(nums, mid+1, right);

    return root;
}

// solution: recursive pre-order dfs
// complexity
// run-time: O(n)
// space: O(log n), max height
TreeNode* sortedArrayToBST(const std::vector<int>& nums)
{
    return dfs(nums, 0, nums.size()-1);
}

// TODO: add unit tests
