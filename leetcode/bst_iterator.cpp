#include <cstddef>
# include <iostream>
#include <vector>

// number: 173
// title: Binary Search Tree Iterator
// url: https://leetcode.com/problems/binary-search-tree-iterator/
// section: binary tree general
// difficulty: medium
// tags: stack, tree, design, bst, binary tree, iterator

// constraints
// The number of nodes in the tree is in the range [1, 10^5].
// 0 <= Node.val <= 10^6
// At most 10^5 calls will be made to hasNext, and next.

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

class BSTIterator {
public:
    // complexity
    // run-time: O(n)
    // space: O(n)
    BSTIterator(TreeNode* root) {
        dfs(root);
    }

    // complexity
    // run-time: O(1)
    // space: O(n)
    int next() {
        ++d_index;
        return d_index < d_nodes.size() ? d_nodes[d_index] : -1;
    }

    // complexity
    // run-time: O(1)
    // space: O(n)
    bool hasNext() {
        return d_index < d_nodes.size()-1;
    }

private:
    void dfs(TreeNode* root) {
        if (!root) {
            return;
        }

        dfs(root->left);
        d_nodes.push_back(root->val);
        dfs(root->right);
    }
    std::vector<int> d_nodes;
    int d_index = -1;
};

int main() {
    TreeNode* root = nullptr;
    // populate the tree as needed
    auto it = BSTIterator(root);
    while (it.hasNext()) {
        std::cout << it.next() << std::endl;
    }
    return 0;
}