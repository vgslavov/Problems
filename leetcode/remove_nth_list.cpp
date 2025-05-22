#include <cstddef>

// number: 19
// title: Remove Nth Node From End of List
// url: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// section: linked list
// difficulty: medium
// tags: linked list, two pointers, top 150

// constraints
// The number of nodes in the list is sz.
// 1 <= sz <= 30
// 0 <= Node.val <= 100
// 1 <= n <= sz

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// solution: dummy node + fast & slow pointers
// complexity
// run-time: O(n)
// space: O(1)
ListNode* removeNthFromEnd(ListNode* head, int n)
{
    ListNode* dummy = new ListNode(0, head);
    ListNode* fast = dummy;
    ListNode* slow = dummy;

    // skip n nodes
    while (fast->next != nullptr && n != 0) {
        fast = fast->next;
        --n;
    }

    // go to end
    while (fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next;
    }

    // skip nth node
    slow->next = slow->next->next;

    // return original head
    return dummy->next;
}

// TODO: add unit tests
