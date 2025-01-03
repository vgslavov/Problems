#include <deque>
#include <vector>

// number: 199
// section: binary tree bfs
// difficulty: medium
// tags: dfs, bfs, binary tree, top 150, meta
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
    if (!root) {
        return std::vector<int>{};
    }

    std::deque<TreeNode*> queue{root};
    std::vector<int> ans;

    while (!queue.empty()) {
        int size = queue.size();
        TreeNode* last_p = queue.back();

        ans.push_back(last_p->val);

        while (size) {
            TreeNode* node_p = queue.front();
            queue.pop_front();

            if (node_p->left) {
                queue.push_back(node_p->left);
            }

            if (node_p->right) {
                queue.push_back(node_p->right);
            }

            --size;
        }
    }

    return ans;
}

// TODO: add unit tests
