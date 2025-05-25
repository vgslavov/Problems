#include <cstddef>
#include <queue>

// number: 117
// title: Populating Next Right Pointers in Each Node II
// url: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
// section: binary tree
// difficulty: medium
// tags: linked list, tree, dfs, bfs, binary tree

// constraints
// The number of nodes in the tree is in the range [0, 6000].
// -100 <= Node.val <= 100

// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val) : val(_val), left(nullptr), right(nullptr), next(nullptr) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

// solution: iterative bfs
// complexity
// run-time: O(n)
// space: O(n)
Node* connect(Node* root)
{
    if (!root) {
        return nullptr;
    }

    std::queue<Node*> queue;
    queue.push(root);

    while (!queue.empty()) {
        int size = queue.size();
        Node* prev_node = nullptr;

        while (!size) {
            Node* node = queue.front();
            queue.pop();

            // link each node to previous one on the same level
            if (prev_node) {
                prev_node->next = node;
            }

            prev_node = node;

            if (node->left) {
                queue.push(node->left);
            }

            if (node->right) {
                queue.push(node->right);
            }

            --size;
        }
    }

    return root;
}
