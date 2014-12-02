// TEST: {0, 1, 2, 3}-sized

typedef struct list {
	int data;
	struct list *next;
} list;

// non-recursive (pointers)
// TESTED
list *
reverse_list(list *head)
{
	list *prev, *cur;

	// 0-sized
	if (head == NULL) return NULL;

	prev = NULL;
	cur = head;
	// 1…n-sized
	while (cur != NULL) {
		head = cur->next;
		cur->next = prev;
		prev = cur;
		cur = head;
	}

	// end of list
	if (cur == NULL)
		head = prev;

	return head;
}

// non-recursive (stack)
list *
reverse_list_stack(list *head)
{
	stack<list *> s;
	list *p;

	// 0-sized
	if (head == NULL) return NULL;

	p = head;
	// put all nodes on stack (LIFO order)
	while (p != NULL) {
		s.push(p);
		p = p->next;
	}

	// pop the stack and connect pointers
	head = p = s.top();
	while (s.size() > 0) {
		p->next = s.top();
		s.pop();
		p = p->next;
	}
	p->next = NULL;

	return head;
}

// recursive
// TEST!
// call reverse_list_rec(head, NULL);
list *
reverse_list_rec(list *head, list *prev)
{
	list *p;

	// base case, 0-sized
	if (head == NULL)
		return prev;
	
	p = head->next;
	head->next = prev;
	return reverse_list_rec(p, head);
}

// recursive (better)
// TEST!
// call reverse_list_rec2(head, NULL);
list *
reverse_list_rec2(list *head, list *prev)
{
	list *p;

	// base case
	// ATTN: better to test head->next, not head!
	if (head->next == NULL) {
		head->next = prev;
		return head;
	} else {
		p = reverse_list_rec2(head->next, head);
		// reverse ptr!
		head->next = prev;
		return p;
	}
}

// recursive (BAD!)
// call reverse_list_rec(head);
list *
reverse_list_rec3(list *head)
{
	list *p, prev;

	p = head->next;
	if (p == NULL) return head;

	prev = reverse_list_rec3(head->next);
	p->next = head;
	head->next = NULL;

	return prev;
}
