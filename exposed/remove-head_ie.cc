// fixed bugs
bool remove_head(ListElement **head)
{
	ListElement *p;

	if ((head == NULL) || (*head == NULL))
		return false;

	p = (*head)->next;
	free(*head);
	*head = p;

	return true;
}