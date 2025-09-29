#include <algorithm>
#include <cstddef>
#include <limits>

// tags: dfs, tree

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

int dfs(TreeNode* node, int max)
{
    if (!node) {
        return 0;
    }

    int total = 0;
    // current node is visible only if
    // greater than anything on the path from root to this node
    if (node->val >= max) {
        ++total;
    }

    return
        dfs(node->left, std::max(max, node->val)) +
        dfs(node->right, std::max(max, node->val)) +
        total;
}

// solution: AlgoMonster recursive dfs
// complexity:
// run-time: O(n)
// space: O(h) average, O(n) worst
int visibleTreeNode(TreeNode* root)
{
    return dfs(root, std::numeric_limits<int>::min());
}