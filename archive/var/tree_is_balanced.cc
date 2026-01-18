typedef struct BinaryTree {
    int data;
    struct BinaryTree *left;
    struct BinaryTree *right;
    struct BinaryTree *parent;
} BinaryTree;

// space: O(n) (on stack)?
bool is_balanced(BinaryTree *t)
{
    return ((max_depth(t) - min_depth(t)) <= 1);
}

int max_depth(BinaryTree *t)
{
    if (!t)
        return 0;

    return 1 + max(max_depth(t->left), max_depth(t->right));
}

int min_depth(BinaryTree *t)
{
    if (!t)
        return 0;

    return 1 + min(min_depth(t->left), min_depth(t->right));
}

// time: O(n)
// space: O(h) stack height is bounded by the height of tree
// (can be improved to O(log n) by keeping track of max height of stack)
bool is_balanced(BinaryTree *t)
{
    return (get_height(t) != -2);
}

// post-order traversal (eliminates calls based on early detection of unbalance)
// return:
// -2: tree is unbalanced
// -1: t is NULL
// int n: height of tree
int get_height(BinaryTree *t)
{
    // base case
    if (!t)
        return -1;

    int l = get_height(t->left);
    // left tree unbalanced
    if (l == -2)
        return -2;

    int r = get_height(t->right);
    // right tree unbalanced
    if (r == -2)
        return -2;

    // current node unbalanced
    if (abs(l - r) > 1)
        return -2;

    // actual height
    return max(l, r) + 1;
}
