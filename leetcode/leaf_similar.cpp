#include <cstddef>
#include <vector>

// number: 872
// section: assessments
// difficulty: easy
// tags: tree, dfs, binary tree, microsoft

// constraints
// The number of nodes in each tree will be in the range [1, 200].
// Both of the given trees will have values in the range [0, 200].

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
void dfs(TreeNode* root, std::vector<int>& leaves)
{
    if (!root) {
        return;
    } else if (!root->left && !root->right) {
        leaves.push_back(root->val);
        return;
    }

    dfs(root->left, leaves);
    dfs(root->right, leaves);
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
bool leafSimilar(TreeNode* root1, TreeNode* root2)
{
    if (!root1 && !root2) {
        return true;
    } else if (!root1 || !root2) {
        return false;
    }

    std::vector<int> leaves1;
    dfs(root1, leaves1);

    std::vector<int> leaves2;
    dfs(root2, leaves2);

    return leaves1 == leaves2;
}
