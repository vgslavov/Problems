// TEST: empty, equal, non-equal, different/same shape only, different/same data only
// O(n)?

// not symmetry!
bool
same_trees(tree *t1, tree *t2)
{
	// both empty
	if ((t1 == NULL) && (t2 == NULL))
		return true;
	// both non-empty
	} else if ((t1 != NULL) && (t2 != NULL)) {
		return (t1->data == t2->data && same_trees(t1->left, t2->left) && same_trees(t1->right, t2->right));
	// one empty
	} else
		return false
}

// symmetry!
bool
compare_trees_all(tree *t1, tree *t2)
{
	if (t1 == t2) return true;

	// one tree ended already
	if ((t1 == NULL) || (t2 == NULL)) return false;

    // pay attention to which children you compare
	return ((t1->data == t2->data) && compare_trees_all(t1->left, t2->right)
				       && compare_trees_all(t1->right, t2->left));
}

bool
is_symmetric(tree *t)
{
	// empty tree
	if (t == NULL) return true;

	return compare_subtrees(t->left, t->right);
}

// symmetry!
bool
compare_subtrees(tree *t1, tree *t2)
{
	if (t1 == t2) return true;

	// one tree ended already
	if ((t1 == NULL) || (t2 == NULL)) return false;

    // pay attention to which children you compare
	return (compare_subtrees(t1->left, t2->right)
		&& compare_subtrees(t1->right, t2->left));
}


