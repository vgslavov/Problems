#include <cstddef>
#include <map>

// number: 138
// section: linked list
// difficulty: medium
// tags: linked list, hash table, top 150

// constraints
// 0 <= n <= 1000
// -10^4 <= Node.val <= 10^4
// Node.random is null or is pointing to some node in the linked list.

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};

Node* createNode(Node* oldNode, std::map<Node *, Node*>& visited)
{
    if (!oldNode) {
        return nullptr;
    }

    auto it = visited.find(oldNode);
    if (it != visited.end()) {
        return it->second;
    }

    Node* newNode = new Node(oldNode->val);
    visited[oldNode] = newNode;

    return newNode;
}

// solution: dict of visited nodes
// complexity
// run-time: O(n)
// space: O(n)
Node* copyRandomList(Node* head)
{
    if (!head) {
        return nullptr;
    }

    std::map<Node *, Node *> visited;
    Node* newNode = new Node(0);
    Node* newHead = newNode;
    Node* prevNode = nullptr;

    while (head != nullptr) {
        newNode->next = createNode(head, visited);

        if (prevNode != nullptr) {
            prevNode->next = newNode;
            prevNode = prevNode->next;
        } else {
            prevNode = newNode;
        }

        newNode = newNode->next;
        newNode->random = createNode(head->random, visited);

        head = head->next;
    }

    return newHead->next;
}

Node* dfs(Node* oldNode, std::map<Node*, Node*>& visited)
{
    if (!oldNode) {
        return nullptr;
    }

    auto it = visited.find(oldNode);
    if (it != visited.end()) {
        return it->second;
    }

    Node* newNode = new Node(oldNode->val);
    visited[oldNode] = newNode;

    newNode->next = dfs(oldNode->next, visited);
    newNode->random = dfs(oldNode->random, visited);

    return newNode;
}

// solution: leetcode recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
Node* copyRandomList2(Node* head)
{
    std::map<Node*,Node*> visited;

    return dfs(head, visited);
}
