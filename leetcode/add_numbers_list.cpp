#include <cstddef>

// number: 2
// title: Add Two Numbers
// url: https://leetcode.com/problems/add-two-numbers/
// section: linked list
// difficulty: medium
// tags: linked list, math, recursion, top 150, meta

// constraints
// The number of nodes in each linked list is in the range [1, 100].
// 0 <= Node.val <= 9
// It is guaranteed that the list represents a number that does not have leading
// zeros.

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// solution: doesn't require reverse
// complexity
// run-time: O(n)
// space: O(1)
ListNode* int2list(long long int num)
{
    ListNode* l = new ListNode();
    ListNode* head = l;

    if (num == 0) {
        return head;
    }

    while (num > 0) {
        l->next = new ListNode(num % 10);
        num /= 10;
        l = l->next;
    }

    return head->next;
}

// complexity
// run-time: O(n)
// space: O(1)
long long int list2int(ListNode* l)
{
    long long int ans = 0;
    long long int digit = 1;

    while (l) {
        ans += l->val * digit;
        // TODO: fix overflow
        digit *= 10;
        l = l->next;
    }

    return ans;
}

// solution: list 2 int 2 list + reverse
// complexity
// run-time: O(n)
// space: O(1)
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
{
    return int2list(list2int(l1) + list2int(l2));
}
