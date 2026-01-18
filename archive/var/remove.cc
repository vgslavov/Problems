// remove specific node in O(1)
// conditions: not last node
void remove_const(Node *rm)
{
    Node *next = rm->next;

    rm->data = next->data;
    rm->next = next->next;
    free(next);
}

// remove k-th last node
// TODO: verify with diff. len lists and values of k
bool remove_kth(Node **L, int k)
{
    Node *ahead = *L;

    while (k-- && ahead) {
        ahead = ahead->next;
    }

    if (k) {
        // k > len
        return false;
    }

    Node *pre = NULL;
    Node *cur = *L;
    // ahead points to k-th node from start
    // check only ahead because it’s ahead!
    while (ahead) {
        pre = cur;
        cur = cur->next;
        ahead = ahead->next;
    }

    // most cases
    if (pre) {
        // skip node 2 delete
        pre->next = cur->next;
        // delete actual node
        free(cur);
        return true;
    // if 1st node?
    } else {
        pre = *L;
        *L = cur->next;
        free(pre);
        return true;
    }
}

// split list in 2
// TODO
void split_list(Node *head, Node **front, Node **back)

// spaces
// 2 pointers!
void remove_spaces(char *str)
{
    char *p1 = str;
    char *p2 = str;

    do {
        while (*p2 == ‘ ‘) {
            ++p2;
        }
        *p1 = *p2;
        ++p1;
        ++p2;
    // TODO: *p1 or p1?
    } while (*p1);
}
