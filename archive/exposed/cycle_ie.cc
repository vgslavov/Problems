bool
cycle(Node *head)
{
	Node *fast, *slow;

	slow = head;
	fast = head->next;

	if (slow == NULL)
		return false;

	while (1) {
		if ((fast == NULL) || (fast->next == NULL))
			return false;
		else if ((fast == slow) || (fast->next == slow))
			return true;
		else {
			slow = slow->next;
			// advance 2 nodes!
			fast = fast->next->next;
		}
	}
}