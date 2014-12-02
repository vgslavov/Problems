// not pointer to struct!
typedef struct stack {
	struct stack *next;
	void *data;
} stack;

// *data is element to push on top
bool push(stack **s, void *data);
// **data is element popped
bool pop(stack **s, void **data);
bool create_stack(stack **s);
bool delete_stack(stack **s);

bool push(stack **s, void *data)
{
	stack *p;

	p = malloc(sizeof(stack));

	if (p == NULL)
		return false;

	p->data = data;
	p->next = *s;
	*s = p;

	return true;
}

bool pop(stack **s, void **data)
{
	stack *p;

	if (*s == NULL)
		return false;

	p = *s;
	*data = p->data;
	*s = p->next;
	free(p);

	return true;
}

bool create_stack(stack **s)
{
	*stack = NULL;
	return true;
}

bool delete_stack(stack **s)
{
	stack *p;

	if (*s == NULL)
		return false;

	while (*s != NULL) {
		p = (*s)->next;
		free(*s);
		*s = p;
	}

	return true;
}

int get_size(stack *s)
{
	int n;

	n = 0;
	while (s != NULL) {
		s = s->next;
		++n;
	}
	return n;
}