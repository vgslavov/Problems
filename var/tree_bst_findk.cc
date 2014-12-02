// first k: recursive
BST *find_first_k(const BST *&t, const int &k)
{
    // no match
    if (!t) {
        return NULL;
    } else if (t->data == k) {
        // diff. with conventional BST search:
        // search left subtree for first one == k
        BST *n = find_first_k(t->left, k);
        return n ? n : t;
    }

    // search right subtree if current is < k
    // search left subtree if current > k
    return find_first_k(t->data < k ? t->right : t->left, k);
}

// first k: iterative
BST *find_first_k(const BST *&t, const int &k)
{
    // candidate node
    BST *first = NULL;
    BST *cur = t;

    while (cur) {
        // go right
        if (cur->data < k) {
            cur = cur->right;
        // go left
        } else if (cur->data > k) {
            cur = cur->left;
        // cur->data == k
        } else {
            // record node
            first = cur;
            // and keep searching left subtree
            cur = cur->left;
        }
    }

    return first;
}

// first larger than k
// O(h) time
// O(1) space
BST *find_first_larger_k(const BST *&t, const int &k)
{
    // candidate node
    BST *first = NULL;
    BST *cur = t;
    bool found_k = false;

    while (cur) {
        // when k is found, record found and go right to look for larger
        if (cur->data == k) {
            found_k = true;
            cur = cur->right;
        // record larger value
        } else if (cur->data > k) {
            first = cur;
        }
        // skip smaller values
    }

    return found_k ? first : NULL;
}

// min-first BST: find k, O(h) time
bool search_min_first_BST(const BST *&t, const &k)
{
    // empty or root is bigger (root is the min node in a min-first BST)
    if (!t || t->data > k) {
        return false;
    // found!
    } else if (t->data == k) {
        return true;
    }

    // if there is a right subtree and its root is smaller than k, go there
    if (t->right && t->right->data <= k)
        search_min_first_BST(t->right, k);

    // finally search left
    return search_min_first_BST(t->left, k);
}
