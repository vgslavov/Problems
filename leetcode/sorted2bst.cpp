#include <cstddef>
#include <vector>

// number: 108
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
    int p = (left+right) / 2;

    // pre-order traversal
    TreeNode* root = new TreeNode(nums[p]);
    root->left = dfs(nums, left, p-1);
    root->right = dfs(nums, p+1, right);

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
