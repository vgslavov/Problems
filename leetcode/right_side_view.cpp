#include <queue>
#include <vector>

// number: 199
// title: Binary Tree Right Side View
// url: https://leetcode.com/problems/binary-tree-right-side-view/
// section: binary tree bfs
// difficulty: medium
// tags: dfs, bfs, binary tree, top 150, meta, grind 75
//
// constraints
// The number of nodes in the tree is in the range [0, 100].
// -100 <= Node.val <= 100

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

// solution: iterative bfs
// complexity
// run-time: O(n)
// space: O(n)
std::vector<int> rightSideView(TreeNode* root)
{
    std::vector<int> ans;

    if (!root) {
        return ans;
    }

    std::queue<TreeNode*> queue;
    queue.push(root);

    while (!queue.empty()) {
        int size = queue.size();
        TreeNode* last_p = queue.back();

        ans.push_back(last_p->val);

        while (size) {
            TreeNode* node_p = queue.front();
            queue.pop();

            if (node_p->left) {
                queue.push(node_p->left);
            }

            if (node_p->right) {
                queue.push(node_p->right);
            }

            --size;
        }
    }

    return ans;
}

// TODO: add unit tests
