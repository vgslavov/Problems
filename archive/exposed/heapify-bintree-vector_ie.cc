std::vector heapify_bintree(tree *t)
{
	// don't need to count # of nodes!

	std::vector<tree *> v;

	// load nodes into vector
	traverse(t, 0, v);

	// sort array of nodes based on value
	// TODO: verify mycmp works
	std::sort(v.begin(), v.end(), mycmp);

	// reassign children for each node
	// TODO: or left:(2i) & right:(2i + 1)?
	for (int i = 0; i < v.size(); i++) {
		int left = 2 * i + 1;
		int right = left + 1;
		// TODO: or v[i].left?
		if (left >= size)
			v[i]->left = NULL;
		else
			v[i]->left = v[left];

		if (right >= size)
			v[i]->right = NULL;
		else
			v[i]->right = v[right];
	}
	return v
}

// recursive
// v is passed by reference!
int traverse(tree *t, int count, std::vector<tree *> &v)
{
	// when only counting nodes or when end of tree is reached
	if (t == NULL) return count;

	if (v != NULL) {
		v.push_back(t);
	}
	++count;

	count = traverse(t->left, count, v);
	count = traverse(t->right, count, v);

	return count;
}

bool mycmp(tree *i, tree *j) { return (i->data < j->data) }