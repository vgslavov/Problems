// no parent pointer, but pointer to root: O(n) time
// postorder walk: the LCA is the 1st node visited after a and b have both been visited
// or recursive preorder walk?
BinaryTree *LCA(BinaryTree *t, BinaryTree *a, BinaryTree *b)
{
    // base case: empty tree
    if (!t) {
        return NULL;
    // one is root => LCA is root
    } else if (t == a || t == b) {
        return t;
    }

    // check both subtrees
    BinaryTree *ltree = LCA(t->left, a, b);
    BinaryTree *rtree = LCA(t->right, a, b);

    // in different subtrees: LCA is root
    if (ltree && rtree) {
        return t;
    // in same subtree: whichever is non-empty (didn’t hit base case)
    } else {
        return ltree ? ltree : rtree;
    }
}

// BST: no parent pointer, but pointer to root:
// prune based on constraints (a->data < LCA < b->data): O(h) time, O(1) space
// assumptions: a->data < b->data
BST *LCA(BST *t, BST *a, BST *b)
{
    BST *p = t;

    while (p->data < a->data || p->data > b->data) {
        // LCA is in right subtree (current is smaller than both a & b)
        while (p->data < a->data) {
            p = p->right;
        }

        // LCA is in left subtree (current is bigger than both a & b)
        while (p->data > b->data) {
            p = p->left;
        }
    }

    // p->data >= a->data && p->data <= b->data
    return p;
}

// parent pointer, no pointer to root: O(h) time, O(1) space
BinaryTree *LCA(BinaryTree *a, BinaryTree *b)
{
    int adepth = get_depth(a);
    int bdepth = get_depth(b);
    int diff = abs(adepth - bdepth);

    // assume a is deeper, swap if not
    if (adepth < bdepth)
        swap(a, b);

    // go up with deeper node until on same level
    while (diff--)
        a = a->parent;

    // now go up with both
    while (a != b) {
        a = a->parent;
        b = b->parent;
    }
    return a;
}

int get_depth(BinaryTree *n)
{
    int depth = 0;

    while (t) {
        ++depth;
        n = n->parent;
    }
    return depth;
}

// parent pointer, no pointer to root: O(max(d_a - d_l, d_b - d_l)) space and time,
// where d_l is depth of LCA
// worst: O(h) space and time (when both are leaves with LCA root)
// the LCA is the 1st node in either sequence (to root) that is common to both sequences
BinaryTree *LCA(BinaryTree *a, BinaryTree *b)
{
    // store visited nodes in hash table/set
    unordered_set<BinaryTree *> hash;

    while (a || b) {
        if (a) {
            // can’t insert because already in set
            // insert returns pair with 2nd being a bool if successful
            if (hash.insert(a).second == false)
                return a;
        }
        a = a->parent;

        if (b) {
            if (hash.insert(b).second == false)
                return b;
        }
        b = b->parent;
    }
    throw invalid_argument(“a and b in different binary trees”);
}
