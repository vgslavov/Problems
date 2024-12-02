#include <algorithm>
#include <deque>
#include <limits>
#include <vector>

// number: 515
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
    std::deque<TreeNode> queue{*root};

    while (!queue.empty()) {
        int rowMax = std::numeric_limits<int>::min();
        int rowLen = queue.size();

        for (int i = 0; i != rowLen; ++i) {
            TreeNode node = queue.front();
            queue.pop_front();

            rowMax = std::max(rowMax, node.val);

            if (node.left) {
                queue.push_back(*node.left);
            }

            if (node.right) {
                queue.push_back(*node.right);
            }
        }
        ans.push_back(rowMax);
    }

    return ans;
}

// TODO: add unit tests
