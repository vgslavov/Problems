#include <utility>

// number: 24
// title: Swap Nodes in Pairs
// url: https://leetcode.com/problems/swap-nodes-in-pairs/
// section: recursion
// difficulty: medium
// tags: linked list, recursion

// constraints
// The number of nodes in the list is in the range [0, 100].
// 0 <= Node.val <= 100

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

void swapPairsHelper(ListNode* head)
{
    // base case
    if (!head || !head->next) {
        return;
    }

    std::swap(head->val, head->next->val);

    return swapPairsHelper(head->next->next);
}

// solution: swap values
// complexity
// run-time: O(n)
// space: O(n)
ListNode* swapPairs(ListNode* head)
{
    if (!head || !head->next) {
        return head;
    }

    ListNode* orgHead = head;

    swapPairsHelper(head);

    return orgHead;
}
