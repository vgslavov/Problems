#include <set>

// number: 1650
// title: Lowest Common Ancestor of a Binary Tree III
// url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
// section: meta
// difficulty: medium
// tags: hash table, two pointers, tree, binary tree, meta

// constraints
// The number of nodes in the tree is in the range [2, 10^5].
// -10^9 <= Node.val <= 10^9
// All Node.val are unique.
// p != q
// p and q exist in the tree.

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};

// solution: traverse
// complexity
// run-time: O(n)
// space: O(n)
Node* traverse(Node* node, std::set<Node*>& path) {
    if (!node->parent) {
        path.insert(node);
        return node;
    }

    path.insert(node);

    return traverse(node->parent, path);
}

Node* lca3(Node* p, Node * q) {
    std::set<Node *> path;
    Node* root = traverse(p, path);

    if (!root) {
        return nullptr;
    }

    while (q) {
        auto it = path.find(q);
        if (it != path.end()) {
            return *it;
        }

        q = q->parent;
    }

    return nullptr;
}