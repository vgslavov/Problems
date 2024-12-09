#include <algorithm>
#include <deque>
#include <vector>

// number: 103
// section: binary tree bfs
// difficulty: medium
// tags: tree, bfs, binary tree, top 150

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

// constraints
// The number of nodes in the tree is in the range [0, 2000].
// -100 <= Node.val <= 100

// solution: iterative bfs
// complexity
// run-time: O(n)
// space: O(n)
std::vector<std::vector<int>> zigzagLevelOrder(TreeNode* root)
{
    std::vector<std::vector<int>> ans;

    if (!root) {
        return ans;
    }

    std::deque<TreeNode *> queue{root};
    bool reverse = false;

    while (!queue.empty()) {
        int levelLen = queue.size();
        std::vector<int> level;

        while (levelLen) {
            TreeNode* node_p = queue.front();
            queue.pop_front();

            level.push_back(node_p->val);

            if (node_p->left) {
                queue.push_back(node_p->left);
            }

            if (node_p->right) {
                queue.push_back(node_p->right);
            }

            --levelLen;
        }

        if (reverse) {
            std::reverse(level.begin(), level.end());
        }

        reverse = !reverse;

        ans.push_back(level);
    }

    return ans;
}

// TODO: add unit tests
