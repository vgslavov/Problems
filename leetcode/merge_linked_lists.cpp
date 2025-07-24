#include <cstddef>

// number: 21
// title: Merge Two Sorted Lists
// url: https://leetcode.com/problems/merge-two-sorted-lists/
// section: linked list
// difficulty: easy
// tags: link list, recursion, top 150, meta, grind 75

// constraints
// The number of nodes in both lists is in the range [0, 50].
// -100 <= Node.val <= 100
// Both list1 and list2 are sorted in non-decreasing order.

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// solution: two pointers
// complexity
// run-time: O(n+m)
// space: O(1)
ListNode* mergeTwoLists(ListNode* list1, ListNode* list2)
{
    ListNode* head = new ListNode();
    ListNode* tail = head;

    while (list1 && list2) {
        if (list1->val < list2->val) {
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }

        tail = tail->next;
    }

    // append remaining list
    tail->next = list1 ? list1 : list2;

    return head->next;
}
