typedef struct Node {
	struct Node *next;
	struct Node *prev;
	struct Node *child;
	int value;
} Node;

void flatten_list(Node *head, Node **tail)
{
	Node *p, *q;

	p = head;
	while (p != NULL) {
		if (p->child != NULL) {
			// append 1st child in list to end
			(*tail)->next = p->child;
			p->child->prev = *tail;

			// find end of children list
			for (q = p->child; q->next != NULL; q = q->next) {
				;
			}

			// update tail
			*tail = q;
		}
		p = p->next;
	}
}