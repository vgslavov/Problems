#include <cstddef>

// tags: dfs, tree

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

TreeNode* findSub(TreeNode* root, TreeNode* subRoot)
{
    if (!root) {
        return nullptr;
    }

    if (root->val == subRoot->val) {
        return root;
    }

    TreeNode* left = findSub(root->left, subRoot);
    if (left) {
        return left;
    }

    return findSub(root->right, subRoot);
}

bool compare(TreeNode* root, TreeNode* subRoot)
{
    // both leaves
    if (!root && !subRoot) {
        return true;
    } else if (!root || !subRoot) {
        return false;
    }

    if (root->val != subRoot->val) {
        return false;
    }

    return compare(root->left, subRoot->left) && compare(root->right, subRoot->right);
}

// solution: recursive dfs
// complexity:
// run-time: O(m*n)?
// space: O(m+n)?
bool subtreeOfAnotherTree(TreeNode* root, TreeNode* subRoot)
{
    if (!root && !subRoot) {
        return true;
    } else if (!root || !subRoot) {
        return false;
    }

    TreeNode* sub = findSub(root, subRoot);

    if (!sub) {
        return false;
    }

    return compare(sub, subRoot);
}

// TODO: solve using AlgoMonster recurisive dfs