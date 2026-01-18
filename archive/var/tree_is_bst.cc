typedef struct BST {
    int data;
    struct BST *left;
    struct BST *right;
} BST;

// compute max key in left subtree and min key in right subtree
// worst O(n^2) time, O(n) space
// see Stanford problems

// recursive: check constraints
// O(n) time, O(h) call stack space
bool isBST(const BST *&t)
{
    return isBST_helper(t, numeric_limits<int>::min(), numeric_limits<int>::max());
}

bool isBST_helper(const BST *&t, const int &lower, const int &upper)
{
    // no more tree
    if (!t) {
        return true;
    // if node’s key is not greater than left subtree or is not less than right subtree,
    // it’s not a BST
    } else if (t->data < lower || t->data > upper) {
        return flase;
    }

    // check ranges of values:
    // go left and look for values b/w min and current AND
    // go right and look for values b/w current and max
    return isBST_helper(r->left, lower, r->data) && isBST_helper(r->right, r->data, upper);
}

// iterative: inorder traversal, record last visited node
// O(n) time, O(1) space
// TODO: finish & understand
bool isBST(const BST *&t)
{
    BST *n = t;

    // value of previously visited node
    int last = numeric_limits<int>::min();
    bool res = true;

    while (n) {
        // go left
        if (n->left) {

        }
    }
}

// BFS: useful when BST property is violated at a node with small depth
// (in right subtree)
// TODO: finish & understand
bool isBST(const BST *&t)
{}
