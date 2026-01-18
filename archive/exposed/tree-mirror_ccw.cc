void
mirror_tree(tree *t)
{
	if (t == NULL)
		return;

	tree *tmp;

	mirror_tree(t->left);
	mirror_tree(t->right);

	tmp = t->left;
	t->left = t->right;
	t->right = tmp;	

}
