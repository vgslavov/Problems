// 1. in-order traversal of a binary tree (iterative) [Yahoo]
// 1.1 recursive
void inorder_iter(Node *t)
{
    if (!t)
        return;

    inorder_iter(t->left);
    cout << t->data << “,”;
    inorder_iter(t->right);
}

// 1.2 iterative using stack
// hard!
void inorder_stack(const Node *t)
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

// 1.3 iterative, see EPI solution
