// O(1)
// balance an unbalanced BST
tree *rotate_right(tree *oldroot)
{
	tree *newroot = oldroot->left;
	oldroot->left = newroot->right;
	newroot->right = oldroot;

	return newroot;
}