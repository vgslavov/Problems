#include <algorithm>
#include <queue>
#include <limits>
#include <vector>

// number: 515
// title: Find Largest Value in Each Tree Row
// url: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
// section: assessments
// difficulty: medium
// tags: tree, dfs, bfs, binary tree, meta

// constraints
// The number of nodes in the tree will be in the range [0, 10^4].
// -2^31 <= Node.val <= 2^31 - 1

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

std::vector<int> largestValues(TreeNode* root)
{
    std::vector<int> ans;

    if (!root) {
        return ans;
    }
    std::queue<TreeNode*> queue;
    queue.push(root);

    while (!queue.empty()) {
        int rowMax = std::numeric_limits<int>::min();
        int rowLen = queue.size();

        for (int i = 0; i != rowLen; ++i) {
            TreeNode* node_p = queue.front();
            queue.pop();

            rowMax = std::max(rowMax, node_p->val);

            if (node_p->left) {
                queue.push(node_p->left);
            }

            if (node_p->right) {
                queue.push(node_p->right);
            }
        }
        ans.push_back(rowMax);
    }

    return ans;
}

// TODO: add unit tests
