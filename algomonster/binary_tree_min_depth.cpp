#include <cstddef>
#include <queue>

// tags: bfs, tree

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
int binaryTreeMinDepth(TreeNode* root)
{
    if (!root) {
        return 0;
    }

    std::queue<TreeNode*> queue;
    queue.push(root);
    // 0-based depth
    int depth = 0;

    while (!queue.empty()) {
        size_t size = queue.size();

        while (size) {
            TreeNode* node_p = queue.front();
            queue.pop();

            if (!node_p->left && !node_p->right) {
                return depth;
            }

            if (node_p->left) {
                queue.push(node_p->left);
            }

            if (node_p->right) {
                queue.push(node_p->right);
            }

            --size;
        }

        ++depth;
    }

    return 0;
}