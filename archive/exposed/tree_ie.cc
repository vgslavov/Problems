// not pointer to struct
typedef struct tree {
	// needed?
	struct tree *parent;
	struct tree *left;
	struct tree *right;
	void *data;
} tree;

// O(log(n))
tree *find_node(tree *t, int value)
{
	while (t != NULL) {
		if (t->data == value)
			break;
		// would else if work?
		if (value < t->data)
			t = t->left;
		else
			t = t->right;

	}
	return t;
}

// recursive
// O(log(n))
tree *find_node2(tree *t, int value)
{
	if (t->data == NULL) return NULL;
	if (t->data == value) return t;

	// would else if work?
	if (value < t->data)
		return find_node2(t->left, value);
	else
		return find_node2(T->right, value);
}

// recursive
// O(n)
int tree_height(tree *t)
{
	// base case
	if (t == NULL) return 0;

	return 1 + max(tree_height(t->left), tree_height(t->right));
}

int max(int val1, int val2)
{
	// worry about ==?
	if (val1 > val2) return val1;
	else return val2;
}