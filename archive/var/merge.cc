// because we store pairs
struct Compare {
    bool operator() (const pair<int, int>& lhs, const pair<int, int>& rhs) const
    {
        return lhs.first > rhs.first;
    }
};

// merge  sorted arrays
// time: O(n logk) (extract-min and insert are O(logk))
// space: O(k)
// similar to files, except no need for tracking the idx of next unprocessed element
// (I/O lib does it)
vector<int> merge_arrays(vector<vector<int> > &S)
{
    // store in min-heap (priority queue with modified Compare operator())
    // p.first: actual value, p.second: index of array it came from
    priority_queue<pair<int, int>, vector<pair<int, int> >, Compare> min_heap;

    // keep track of already processed elements for each S[i]
    // if S[i][2] is processed, S_idx[i] == 3
    vector<int> S_idx(S.size(), 0);

    // put the 1st element (smallest) of each array in heap
    for (int i = 0; i < S.size(); i++) {
        if (S[i].size() > 0) {
            min_heap.push(S[i][0], i);
            // array i’s first element has been processed
            S_idx[i] = 1;
        }
    }

    // one giant sorted array (to return)
    vector<int> ret;

    while(!min_heap.empty()) {
        // get smallest element from heap and put it in ret
        pair<int, int> p = min_heap.top();
        ret.push_back(p.first);

        // make sure this is not the last element of array S[p.second]
        if (S_idx[p.second] < S[p.second].size()) {
            // put the next element from the array with the smallest element in heap
            min_heap.push(S[p.second][S_idx[p.second]++], p.second);

            // ATTN: S_idx[p.second] was updated/incremented in-place above!
        }

        // TODO: does it matter if popping is done now or right after top?
        min_heap.pop();
    }

    return ret;
}

// lists
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// sorted lists: simple
Node *merge_lists(Node *L, Node *F)
{
    Node *newhead;
    Node *p;

    if (L->data > F->data) {
        newhead = F;
        F = F->next;
    // L is < or =
    } else {
        newhead = L;
        L = L->next;
    }

    // p is always one behind
    p = newhead;
    while (L && F) {
        if (L->data > F->data) {
            p->next = F;
            F = F->next;
        // L is < or =
        } else {
            p->next = L;
            L = L->next;
        }
        p = p->next;
    }

    // append remaining L
    if (L) {
        p->next = L;
    }

    // append remaining F
    if (F) {
        p->next = F;
    }
    return newhead;
}

// sorted lists: more elegant
// TODO: double-check ptr to ptr code
Node *merge_lists(Node *L, Node *F)
{
    Node *newhead = NULL;
    Node *tail = NULL;

    while (L && F) {
        // works for == too
        append_and_adv(&newhead, &tail, F->data < L->data ? &F : &L);
    }

    // append remaining L
    if (L) {
        append(&newhead, &tail, &L);
    }

    // append remaining F
    if (F) {
        append(&newhead, &tail, &F);
}
    return newhead;
}

// C++: & to operate by ref (no need to use & when calling)
//void append_and_adv(Node *&head, Node *&tail, Node *&cur)
// C: ptr to ptr
void append_and_adv(Node **head, Node **tail, Node **cur)
{
    append(head, tail, cur);
    *cur = (*cur)->next;
}

// C++: & to operate by ref (no need to use & when calling)
//void append(Node *&head, Node *&tail, Node *&cur)
// C: ptr to ptr
void append(Node **head, Node **tail, Node **cur)
{
    if (*head)
        (*tail)->next = *cur;
    // empty list
    else
        *head = *cur;

    // set to new last node (works for empty list too)
    *tail = *cur;
}

// find overlap in lists: O(n)
Node *find_overlap(Node *L1, Node *L2)
{
    int len1 = calc_length(L1);
    int len2 = calc_length(L2);

    // advance longer list by diff in lengths (the length of common nodes)
    adv_by_k(len1 > len2 ? &L1 : &L2, abs(len1 - len2));

    // advance both
    while (L1 && L2 && L1 != L2) {
        L1 = L1->next;
        L2 = L2->next;
    }
    // if NULL, no overlap
    return L1;
}

int calc_length(Node *L)
{
    int len = 0;

    while(L) {
        ++len;
        L = L->next;
    }
    return len;
}

void adv_by_k(Node **L, int k)
{
    while (k) {
        *L = (*L)->next;
        --k;
    }
}
