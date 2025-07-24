#include <deque>
#include <vector>

// number: 102
// title: Binary Tree Level Order Traversal
// url: https://leetcode.com/problems/binary-tree-level-order-traversal/
// section: binary tree bfs
// difficulty: medium
// tags: tree, bfs, binary tree, top 150, grind 75
//
// constraints
// The number of nodes in the tree is in the range [0, 2000].
// -1000 <= Node.val <= 1000

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// solution: iterative bfs
// complexity
// run-time: O(n)
// space: O(n)
std::vector<std::vector<int>> levelOrder(TreeNode* root)
{
    std::vector<std::vector<int>> ans;

    if (!root) {
        return ans;
    }

    std::deque<TreeNode*> queue{root};

    while (!queue.empty()) {
        int rowLen = queue.size();
        ans.push_back(std::vector<int>());

        for (int i = 0; i != rowLen; ++i) {
            TreeNode* node_p = queue.front();
            queue.pop_front();

            ans[ans.size()-1].push_back(node_p->val);

            if (node_p->left) {
                queue.push_back(node_p->left);
            }

            if (node_p->right) {
                queue.push_back(node_p->right);
            }
        }
    }

    return ans;
}

// TODO: add unit tests
