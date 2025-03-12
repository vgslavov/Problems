#include <cstddef>

// number: 148
// section: divide & conquer
// difficulty: medium
// tags: linked list, two pointers, divide & conquer, sorting, merge sort,
// top 150

// constraints
// The number of nodes in the list is in the range [0, 5 * 10^4].
// -10^5 <= Node.val <= 10^5

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// run-time: O(n)
ListNode* merge(ListNode* list1, ListNode* list2)
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

    tail->next = list1 ? list1 : list2;

    return head->next;
}

// run-time: O(n)
ListNode* findMid(ListNode* head)
{
    if (!head) {
        return nullptr;
    }

    ListNode* prev = nullptr;
    ListNode* mid = head;

    while (head && head->next) {
        prev = mid;
        mid = mid->next;
        head = head->next->next;
    }

    // disconnect
    prev->next = nullptr;

    return mid;
}

// solution: LeetCode fast/slow ptrs + merge sort
// complexity:
// run-time: O(n*log n)
// space: O(log n)
ListNode* sortList(ListNode* head)
{
    // base case: return head!
    if (!head || !head->next) {
        return head;
    }

    ListNode* mid = findMid(head);
    ListNode* left = sortList(head);
    ListNode* right = sortList(mid);

    return merge(left, right);
}
