#include <limits>
#include <vector>

// number: 530
// section: binary search tree
// difficulty: easy
// tags: tree, dfs, bfs, binary search tree, binary tree, top 150

// constraints
// The number of nodes in the tree is in the range [2, 10^4].
// 0 <= Node.val <= 10^5

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

void dfs(TreeNode* root, std::vector<int>& vals)
{
    if (root == nullptr) {
        return;
    }

    // in-order traversal
    dfs(root->left, vals);
    vals.push_back(root->val);
    dfs(root->right, vals);
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
int getMinimumDifference(TreeNode* root)
{
    int minDiff = std::numeric_limits<int>::max();

    std::vector<int> nums;
    dfs(root, nums);

    for (size_t i = 0; i != nums.size()-1; ++i) {
        minDiff = std::min(minDiff, abs(nums[i]-nums[i+1]));
    }

    return minDiff;
}

// TODO: add unit tests
