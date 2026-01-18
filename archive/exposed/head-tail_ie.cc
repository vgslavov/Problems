bool delete(Element *elem)
{
	Element *p;

	// can't delete non-existing element
	if (elem == NULL)
		return false;

	// 0-sized list
	if (head == NULL)
		return false;

	// elem is 1st: head changes
	if (elem == head) {
		head = elem->next;
		// 1-sized list
		if (head == NULL)
			tail = NULL;
		free(elem);
		return true;
	}

	p = head;
	while (p != NULL) {
		// stop at predecessor elem!
		if (p->next == elem) {
			p->next = elem->next;
			// elem is last: tail changes
			if (p->next == NULL)
				tail = p;
			free(elem);
			return true;
		}
		p = p->next;
	}

	// elem not found
	if (p == NULL)
		return false;
}

bool insertAfter(Element *elem, int data)
{
	Element *p, *new;

	new = malloc(sizeof(Element));
	if (new == NULL)
		return false;
	new->data = data;

	// at the beginning
	if (elem == NULL) {
		new->next = head;
		head = new;
		// 0-sized list
		if (tail == NULL)
			tail = new;
		return true;
	}

	p = head;
	while (p != NULL) {
		// stop at elem!
		if (p == elem) {
			new->next = elem->next;
			elem->next = new;

			// at the end
			if (new->next == NULL)
				tail = new;

			return true;
		}
		p = p->next;
	}

	// elem not found
	if (p == NULL) {
		// don't forget!
		free(new);
		return false;
	}
}