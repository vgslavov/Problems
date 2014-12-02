typedef struct Node {
    int data;
    struct Node *next;
} Node;

// hash table: store visited nodes in it (O(n) space)

// bit fiddling: set LSB of next pointer to mark visited nodes

// reverse list: cycle if head is encountered during reversal (O(n) time, O(1))

// two loops (brute-force): cycle if a node in outer loop is visited twice (O(n^2))

// fast and slow ptrs: O(n)
Node *cycle(Node *head)
{
    Node *fast = head;
    Node *slow = head;

    while (slow && fast && fast->next) {
        // 1st advance!
        slow = slow->next;
        fast = fast->next->next;

        // then check
        // TODO: is 2nd == needed?
        if (slow == fast || slow == fast->next) {
            return slow;
        }
    }
    return NULL;
}

// detect & find start of cycle
// O(n): both ptrs to reach the cycle (O(F)) +
//       overlap once slower enters cycle (O(C))
Node *cycle(Node *head)
{
    Node *fast = head;
    Node *slow = head;

    // check all possible ptr references!
    while (slow && slow->next & fast && fast->next && fast->next->next) {
        // 1st advance!
        slow = slow->next;
        fast = fast->next->next;

        // then check
        // TODO: only one is needed?
        if (slow == fast) {
            // find cycle len
            int clen = 0;
            do {
                ++clen;
                fast = fast->next;
            } while (slow != fast);

            // set to beginning
            fast = head;
            slow = head;
            // advance fast by clen
            while (clen) {
                fast = fast->next;
                --clen;
            }

            // advance both
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            // start of cycle
            return slow;
        }
    }
    // no cycle
    return NULL;
}

// find median of sorted circular list
double find-median(Node *ptr)
{
    // empty list
    if (!ptr)
        return -1;

    // find beginning of list (smallest node)
    int len = 0;
    Node *start = ptr;
    Node *cur = ptr;
    do {
        ++len;
        cur = cur->next;
        // make start always point to largest node
        if (start->data <= cur->data) {
            start = cur;
        }
    } while (cur != ptr);
    // start points to largest now, next is smallest (beginning)
    start = start->next;

    // traverse to middle of list
    for (int i = 0; i < ((len - 1) >> 1); i++) {
        start = start->next;
    }

    // odd length
    if ((len & 1) == 1)
        return start->data;
    else
        return (start->data + start->next->data) / 2;
}
