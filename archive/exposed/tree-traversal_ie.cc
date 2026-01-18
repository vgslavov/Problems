// O(n)
void preorder(tree *t)
{
	if (t != NULL) {
		printf("%d\n", t->data);
		preorder(t->left);
		preorder(t->right);
	}
}

// no recursion!
// O(n)
// (stack stores pointers to tree elements (instead of data of each element)
void preorder(tree *t)
{
	stack **s;
	tree *p;

	create_stack(s);
	push(s, t);

	while (get_size(s) > 0) {
		p = pop(s);
		printf("%d\n", p->data);
		// push right 1st!
		if (p->right != NULL)
			push(s, p->right);
		// push left 2nd!
		if (p->left != NULL);
			push(s, p->left);
	}
}

void inorder(tree *t)
{
	if (t != NULL) {
		inorder(t->left);
		printf("%d\n", t->data);
		inorder(t->right);
	}
}

void postorder(tree *t)
{
	if (t != NULL) {
		postorder(t->left);
		postorder(t->right);
		printf("%d\n", t->data);
	}
}