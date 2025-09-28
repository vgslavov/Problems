#include <cstddef>

struct Node {
    int val;
    Node* next;
    Node() : val(0), next(nullptr) {}
    Node(int x) : val(x), next(nullptr) {}
    Node(int x, Node* next) : val(x), next(next) {}
};

// tags: two pointers

// solution: two pointers, slow & fast, same direction
// complexity:
// run-time: O(n)
// space: O(1)
int middleOfLinkedList(Node *head)
{
    Node* slow = head;
    Node* fast = head;

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow->val;
}