// find m2last element (data), not pointer (ask!)
bool find_m2last(ListElement *head, int m, void *data)
{
	ListElement *p, *mp;
	int n;

	if (head == NULL)
		return false;

	p = head;
	n = 0;
	while ((p != NULL) && (n < m)) {
		p = p->next;
		++n;
	}

	// check if m == n?

	// list length < m
	if (p == NULL)
		return false;

	mp = head;
	while ((p != NULL) {
		p = p->next;
		mp = mp->next;
	}

	data = mp->data;

	return true;
}