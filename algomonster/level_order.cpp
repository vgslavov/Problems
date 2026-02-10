#include <cstddef>
#include <queue>
#include <vector>

// tags: bfs, tree
// leetcode: 102

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// solution: iterative bfs
// complexity:
// run-time: O(n)
// space: O(n)
std::vector<std::vector<int>> levelOrderTraversal(TreeNode* root)
{
    std::vector<std::vector<int>> ans;

    if (!root) {
        return ans;
    }

    std::queue<TreeNode*> queue;
    queue.push(root);

    while (!queue.empty()) {
        size_t size = queue.size();
        std::vector<int> curr;

        while (size) {
            TreeNode* node_p = queue.front();
            queue.pop();

            curr.push_back(node_p->val);

            if (node_p->left) {
                queue.push(node_p->left);
            }

            if (node_p->right) {
                queue.push(node_p->right);
            }

            --size;
        }

        ans.push_back(curr);
    }

    return ans;
}