// symmetry: structurally symmetric and same keys!

bool is_symmetric(BinaryTree *t)
{
    // empty trees are symmetric
    return !t || is_symmetric_helper(t->left, t->right);
}

bool is_symmetric_helper(BinaryTree *l, BinaryTree *r)
{
    // both ended
    if (!l && !r) {
        return true;
    // both still going
    } else if (l && r) {
        // check value of node and keep going down:
        // compare left subtree of left tree and right subtree of right tree and vice versa!
        return l->data == r->data && is_symmetirc_helper(l->left, r->right)
                         && is_symmetric_helper(l->right, r->left);
    // one ended before the other: (l && !r) || (!l && r)
    } else {
        return false;
    }
}
