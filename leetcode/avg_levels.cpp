#include <deque>
#include <vector>

// number: 637
// section: binary tree BFS
// difficulty: easy
// tags: tree, dfs, bfs, binary tree, top 150

// constraints
// The number of nodes in the tree is in the range [1, 10^4].
// -2^31 <= Node.val <= 2^31 - 1

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

// solution: iterative bfs using deque
// complexity
// run-time: O(n)
// space: O(n)
std::vector<double> averageLevels(TreeNode* root)
{
    std::deque<TreeNode*> queue{root};
    std::vector<double> ans;

    while (!queue.empty()) {
        int size = queue.size();
        double levelSum = 0;

        for (int i = 0; i != size; ++i) {
            TreeNode* node_p = queue.front();
            queue.pop_front();

            levelSum += node_p->val;

            if (node_p->left) {
                queue.push_back(node_p->left);
            }

            if (node_p->right) {
                queue.push_back(node_p->right);
            }
        }

        ans.push_back(levelSum/size);
    }

    return ans;
}

// TODO: add unit tests
