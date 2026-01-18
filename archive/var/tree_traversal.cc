typedef struct BinaryTree {
    int data;
    struct BinaryTree *left;
    struct BinaryTree *right;
    // not always available
    struct BinaryTree *parent;
} BinaryTree;

// tree: an undirected connected acyclic graph

// depth: # of nodes on the search path from the root to n (not including n!)
// height: max depth of any node

// full binary tree: every node other than the leaves has 2 children

// perfect binary tree: a full binary tree WITH:
// - all leaves at the same depth AND
// - evevery parent with 2 children

// complete binary tree:
// - every level (except possibly last) is completely filled
// - all nodes are as far left as possible

// balanced binary tree: one of the following
// - perfect bin tree
// - complete bin tree
// - one where the diff b/w min and max height is <= 1

// height (of a complete binary tree): floor(lg(n))
// # of leaves (perfect binary tree): 2^h
// # of nodes (perfect binary tree): 2^(h+1) - 1
// # of nonleaf nodes (full binary tree): one less than the # of leaves?

// in-order:
// on every node: traverse-left, visit-root, traverse-right;
// adv: left-to-right sweep!
// D, C, E, B, F, H, G, A, J, L, M, K, N, I, O, P

// pre-order:
// on every node: visit-root, traverse-left, traverse-right
// adv: VISIT by going as deep as possible!
// A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P

// post-order:
// on every node: traverse-left, traverse-right, visit-root
// adv: TRAVERSE by going as deep as possible!
// D, E, C, H, G, F, B, M, L, N, K, J, P, O, I, A

// in-order: recursive
// time: O(n)
// space: O(n) or O(h)?
void inorder_recursive(BST *t)
{
    if (t != NULL) {
        inorder(t->left);
        cout << t->data “, “;
        inorder(t->right);
    }
}

// in-order: iterative (ala DFS using stack)
// print sorted order (BST)
void inorder_stack(BST *t)
{
    stack<BST *> s;
    BST *cur = t.get();

    // proceed as long as there is something in the stack OR there is a left child
    while (!s.empty() || cur) {
        // there is left child: push on stack and go left
        if (cur) {
            s.push(cur);
            cur = cur->left.get();
        // no more left children, pop stack and go right
        } else {
            cur = s.top();
            s.pop();
            cout << cur->data << “, “;
            cur = cur->right.get();
        }
    }
}

// time: O(n)
// space: O(n) or O(h)?
void inorder_stack2(const Node *t)
{
    stack<Node *> s;
    Node *p = t;

    while (!s.empty() || p) {
        if (p) {
            s.push(p);
            // ATTN: don’t check for NULL!
            p = p->left;
        } else {
            p = s.top();
            s.pop();
            cout << p->data << “,”;
            // ATTN: don’t check for NULL!
            p = p->right;
        }
    }
}

// in-order: iterative with parent field
// time: O(n)
// space: O(1)!
// TODO: understand better
void inorder_const(Binary Tree *t)
{
    // empty tree
    if (!t)
        return;

    BinaryTree *prev = NULL;
    BinaryTree *cur = t;
    BinaryTree *next;
    while (cur) {
        // 1st iter: no prev OR at left/right child of prev
        if (!prev || prev->left == curr || prev->right == cur) {
            // there is a left child, next go left
            if (cur->left) {
                next = cur->left;
            // no left child
            } else {
                // print current
                cout << cur->data << endl;
                // if right child, go right, otherwise back to parent
                next = (cur->right ? cur->right : cur->parent);
            }
        // this was a left child?
        } else if (cur->left == prev) {
            cout << cur->data << endl;
            next = (cur->right ? cur->right : cur->parent);
        // this was a right child?: cur->right == prev
        } else {
            next = cur->parent;
        }
        // done, move to next
        prev = cur;
        cur = next;
    }
}

// level order: 2 queues (ala BFS using queues)
void print_levels_2qs(BinaryTree *root)
{
    if (!root)
        return;

    queue<BinaryTree *> curlevel;
    queue<BinaryTree *> nextlevel;

    curlevel.push(root);
    while (!curlevel.empty()) {
        BinaryTree *curnode = curlevel.front();
        // it doesn’t matter if you pop before or after getting children
        curlevel.pop();
        cout << curnode->data << “ “;

        // put children (if any) in nextlevel queue
        if (curnode->left)
            nextlevel.push(curnode->left);
        if (curnode->right)
            nextlevel.push(curnode->right);

        // done with current level, go to next by swapping queues
        if (curlevel.empty()) {
            cout << endl;
            swap(curlevel, nextlevel);
        }
    }
}

// level order: 1 queue + counter (ala BFS)
// time: O(n) where n is # of nodes
// space: O(m) where m is max # of nodes on a level (worst is n for full bin tree)
void print_levels_1q(BinaryTree *root)
{
    if (!root)
        return;

    // both current level (l) and next level (l+1) stored one after the other
    queue<BinaryTree *> q;

    q.push(root);

    // # of nodes at level l left to be processed
    int count = q.size();

    while (!q.empty()) {
        BinaryTree *curnode = q.front();
        cout << curnode->data << “ “;

        // ATTN: does order of pop and push matter?
        q.pop();
        --count;

        // done with this level
        if (!curr)
            continue;

        if (curnode->left)
            q.push(curnode->left);

        if (curnode->right)
            q.push(curnode->right);


        // end of level
        if (count == 0) {
            cout << endl;
            // # of nodes on next level (all already in queue)
            count = q.size();
        }
    }
}

// in-order successor with parent field
// time: O(h)
// space: O(1)
BinaryTree *find_successor(BinaryTree *t)
{
    // non-empty right subtree: left-most element in it
    if (t->right) {
        t = t->right;
        while (t->left) {
            t = t->left;
        }
        return t;
    }

    // empty right subtree: first ancestor whose left child is t
    // (that parent is the successor)
    while (t->parent && t->parent->left == t) {
        t = t->parent;
    }

    // if NULL (reached root whose parent ptr is NULL), no successor
    return t->parent;
}

// in-order k-th node: O(n)
// TODO

// in-order k-th node with size field
// time: O(h)
// space: O(1)
BinaryTree *find_kth_node(BinaryTree *t, int k)
{
    while (t) {
        // is there a left subtree
        int lsize = t->left ? t->left->size : 0;

        // k-th node is in right subtree, go there
        if (lsize < k - 1) {
            // modify k (account for left subtree size):
            // k is now the k - (lsize + 1) node of right subtree
            k -= (lsize + 1);
            t = t->right;
        // k-th node is the root/current
        } else if (lsize == k - 1) {
            return t;
        // k-th node is in the left subtree, go there
        } else {
            t = t->left;
        }
    }
    throw length_error(“no k-th node”);
}

// connect leaves of binary tree: O(n)
list<BinaryTree *> connect_leaves(BinaryTree *t)
{
    list<BinaryTree *> l;

    connect_leaves_helper(t, l);

    return l;
}

// C++ call-by-ref
void connect_leaves_helper(BinaryTree *t, list<BinaryTree *> &l)
{
    if (t) {
        // leaf (no children)
        if (!t->left && !t->right) {
            l.push_back(t);
        } else {
            // first push left so that left leaves get pushed first
            // TODO: check if ‘l’ arg is correct
            connect_leaves_helper(t->left, l);
            connect_leaves_helper(t->right, l);
        }
    }
}
