#include <cstddef>
#include <queue>
#include <vector>

// tags: bfs, tree

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

// solution: iterative bfs + deque
// complexity:
// run-time: O(n)
// space: O(n)
std::vector<std::vector<int>> zigZagTraversal(TreeNode* root)
{
    std::vector<std::vector<int>> ans;

    if (!root) {
        return ans;
    }

    std::queue<TreeNode*> queue;
    queue.push(root);
    bool reverse = false;

    while (!queue.empty()) {
        size_t size = queue.size();
        std::deque<int> curr;

        while (size) {
            TreeNode* node_p = queue.front();
            queue.pop();

            if (reverse) {
                curr.push_front(node_p->val);
            } else {
                curr.push_back(node_p->val);

            }

            if (node_p->left) {
                queue.push(node_p->left);
            }

            if (node_p->right) {
                queue.push(node_p->right);
            }

            --size;
        }

        reverse = !reverse;
        ans.push_back(std::vector<int>(curr.begin(), curr.end()));
    }

    return ans;
}