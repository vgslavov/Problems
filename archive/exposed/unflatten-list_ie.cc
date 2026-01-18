void unflatten_list(Node *start, Node **tail)
{
	Node *p;

	explore_separate(start);

	// find last node
	for (p = start; p != NULL; p->next)
		;

	*tail = p;
}

void explore_separate(Node *start)
{
	Node *p;

	p = *start;
	while (p != NULL) {
		if (p->child != NULL) {
			// separate:
			// 1. terminate the list before this child
			p->child->prev->next = NULL;
			// 2. start the children list (this child is 1st)
			p->child->prev = NULL;
			explore_separate(p->child);
		}
		p = p->next;
	}
}