// TEST: 1-element tree, balanced tree, non-balanced tree

bool
is_balanced(tree *t)
{
	return ((max_depth(t) - min_depth(t)) <= 1);
}

int
max_depth(tree *t)
{
	// TODO: do this instead (to return depth of 1 in case of 1-element)?
	//if (t->left == NULL && t->right == NULL) return 0;
	if (t == NULL) return 0;

	return 1 + max(max_depth(t->left), max_depth(t->right));
}

int
min_depth(tree *t)
{
	if (t == NULL) return 0;

	return 1 + min(min_depth(t->left), min_depth(t->right));
}
