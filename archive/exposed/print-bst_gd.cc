// two queues
int
print_bst(tree *t)
{
	tree *p;
	queue<tree *> currentl;
	queue<tree *> nextl;

	if (t == NULL) return -1;

	currentl.push(t);

	while (1) {
		p = currentl.front();
		currentl.pop();
		if (p != NULL) {
			cout << p->data << " ";
			nextl.push(p->left);
			nextl.push(p->right);
		}
		if (currentl.empty() == 0) {
			cout << endl;
			// TODO: verify it works
			swap(currentl, nextl);
			// or copy
			//copy(nextl.front(), nextl.back(), currentl.begin());
		}
	}
}

// one queue (like BFS?)
int
print_bst2(tree *t)
{

}