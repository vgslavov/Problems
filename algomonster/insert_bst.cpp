#include <cstddef>

// tags: dfs, bst

struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int v) : val(v), left(nullptr), right(nullptr) {}
};

// solution: recursive dfs
// complexity:
// run-time: O(n)
// space: O(n)
Node* insertBST(Node* bst, int val)
{
    if (!bst) {
        return new Node(val);
    }

    if (val > bst->val) {
        bst->right = insertBST(bst->right, val);
    } else if (val < bst->val) {
        bst->left = insertBST(bst->left, val);
    }

    return bst;
}