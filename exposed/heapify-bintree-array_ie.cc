// O(n log(n))
// vs. heapifying the starting tree: O(n)
tree *heapify_bintree(tree *t)
{
	// count nodes
	int size = traverse(t, 0, NULL);

	tree *a[size];

	// load nodes into array
	traverse(t, 0, a);

	// sort array of nodes based on value
	// TODO: verify mycmp works
	std::sort(std::begin(a), std::end(a), mycmp);

	// reassign children for each node
	// TODO: or left:(2i) & right:(2i + 1)?
	for (int i = 0; i < size; i++) {
		int left = 2 * i + 1;
		int right = left + 1;
		// TODO: or a[i].left?
		if (left >= size)
			a[i]->left = NULL;
		else
			a[i]->left = a[left];

		if (right >= size)
			a[i]->right = NULL;
		else
			a[i]->right = a[right];
	}
	// TODO: a or *a?
	return a;
}

// recursive
int traverse(tree *t, int count, tree **a)
{
	// when only counting nodes or when end of tree is reached
	if (t == NULL) return count;

	// TODO: check if a or *a!
	if (a != NULL) {
		*a[count] = t;
	}
	++count;

	count = traverse(t->left, count, a);
	count = traverse(t->right, count, a);

	return count;
}

bool mycmp(tree *i, tree *j) { return (i->data < j->data) }