#include <cstddef>
#include <queue>
#include <vector>

// tags: bfs, tree
// leetcode: 199

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
std::vector<int> rightSideView(TreeNode* root)
{
    if (!root) {
        return std::vector<int>{};
    }

    std::queue<TreeNode*> queue;
    queue.push(root);
    std::vector<int> ans;

    while (!queue.empty()) {
        size_t size = queue.size();

        int curr = 0;

        while (size) {
            TreeNode* node_p = queue.front();
            queue.pop();

            curr = node_p->val;

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