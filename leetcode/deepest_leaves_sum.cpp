#include <queue>

// number: 1302
// section:
// difficulty: medium
// tags: tree, dfs, bfs, binary tree

// constraints
// The number of nodes in the tree is in the range [1, 10^4].
// 1 <= Node.val <= 100

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
int deepestLeavesSum(TreeNode* root)
{
    std::queue<TreeNode*> queue;
    queue.push(root);
    int ans = 0;

    while (!queue.empty()) {
        int len = queue.size();
        ans = 0;

        for (size_t i = 0; i != len; ++i) {
            TreeNode* node_p = queue.front();
            queue.pop();

            ans += node_p->val;

            if (node_p->right) {
                queue.push(node_p->right);
            }

            if (node_p->left) {
                queue.push(node_p->left);
            }
        }
    }

    return ans;
}
