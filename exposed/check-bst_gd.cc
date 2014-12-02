// O(n)
// in-order traversal
bool
check_bst(tree *t, int t->data)
{
	// ATTN: static!
	static tree *prev = NULL;

	if (t != NULL) {
		if (check_bst(t->left) == false)
			return false;

		// doesn't work with duplicate-valued nodes
		if (prev != NULL && t->data <= prev->data)
			return false;

		prev = t;

		return check_bst(t->right);
	}
	return true;
}

// Stanford
int isBST(struct node* node) {
  if (node == NULL)
    return(true);

  // false if the min of the left is > than us
  if (node->left!=NULL && minValue(node->left) > node->data)
    return (false);

  // false if the max of the right is <= than us
  if (node->right!=NULL && maxValue(node->right) <= node->data)
    return(false);

  // false if, recursively, the left or right is not a BST
  if (!isBST(node->left) || !isBST(node->right))
    return(false);

  // passing all that, it's a BST
  return(true);
}

/*
 Returns true if the given tree is a binary search tree
 (efficient version).
*/
int isBST2(struct node* node) {
  return(isBSTUtil(node, INT_MIN, INT_MAX));
}

/*
 Returns true if the given tree is a BST and its
 values are >= min and <= max.
*/
int isBSTUtil(struct node* node, int min, int max) {
  if (node == NULL)
    return(true);

  // false if this node violates the min/max constraint
  if (node->data < min || node->data > max)
    return(false);

  // otherwise check the subtrees recursively,
  // tightening the min or max constraint
  return
    isBSTUtil(node->left, min, node->data) &&
    isBSTUtil(node->right, node->data+1, max)
  );
}
