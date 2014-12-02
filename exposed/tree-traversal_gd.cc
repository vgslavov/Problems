// iterative (use stack)
void
tree_traversal(tree *t)
{
	stack<tree *> s;
	tree *p;

	s.push(t);

	while (s.size() > 0) {
		// preorder
		p = s.top();
		s.pop();
		cout << p->data << endl;
		// push right 1st!
		if (p->right != NULL) {
			s.push(p->right);
		}
		if (p->left != NULL) {
			s.push(p->left);
		}
	}
}