/* TEST:

     1
   /   \	
  2     3
 / \   / \
4   5 6   7
 \
  8

*/

// O(log(n))
// BST
tree *
find_lca_byval(tree *t, int val1, int val2)
{
	if (t == NULL) return NULL;

	while (t != NULL) {
		if ((val1 < t->data) && (val2 < t->data))
			t = t->left;
		else if ((val1 > t->data) && (val2 > t->data))
			t = t->right;
		// lca is b/w val1 and val2!
		else
			return t;
	}
}

// recursive
// BST
tree *
find_lca_byptr(tree *t, tree *val1, tree *val2)
{
	if (t == NULL || val1 == NULL || val2 == NULL) return NULL;

	return find_lca_byval(t, val1->data, val2->data);
}

int
height(tree *t)
{
	int height = 0;

	while (t != NULL) {
		t = t->p;
		++height;
	}
	return height;
}

// binary tree
tree *
find_lca(tree *val1, tree *val2)
{
	// get distance of both paths to root
	int h1 = height(val1);
	int h2 = height(val2);
	int diff;
	
	// calculate difference of distances
	if (h2 - h1 < 0)
		diff = h1 - h2;
	else
		diff = h2 - h1;

	// val1 is deeper than val2
	if (h1 > h2) {
		// advance deeper node (val1) diff levels to be at same node as val2
		while (diff > 0) {
			val1 = val1->p;
			--diff;
		}

		// val1 now is at same level as val2
		while (val1 != NULL & val2 != NULL) {
			if (val1 == val2)
				return val1;

			val1 = val1->p;
			val2 = val2->p;
		}
	// val2 is deeper than val1
	} else {
		// advance deeper node (val2) diff levels to be at same node as val1
		while (diff > 0) {
			val2 = val2->p;
			--diff;
		}

		// val2 now is at same level as val1
		while (val1 != NULL & val2 != NULL) {
			if (val1 == val2)
				return val1;

			val1 = val1->p;
			val2 = val2->p;
		}
	}
	// only if val1 and val2 are in different trees
	return NULL;
}

// BAD!
tree *
find_lca(tree *val1, tree *val2)
{
    while (val1->p != NULL || val2->p != NULL) {
        if (val1->p == val2->p) {
                return val1->p;
        } else {
                if (val1->p != NULL)
                    val1 = val1->p;
                if (val2->p != NULL)
                    val2 = val2->p;
        }
    }
    return NULL;
}
