// TEST: empty, cycle, no cycle
// O(n)

bool
cycle(list *head)
{
	list *slowp, *fastp;

	slowp = head;
	fastp = head->next;

	// empty list
	if (slowp == NULL)
		return false;

	// ATTN: check both because fastp skips nodes!
	while (fastp != NULL && fastp->next != NULL) {
		if (fastp == slowp || fastp->next == slowp) {
			return true;
		} else {
			slowp = slowp->next;
			// skip a node
			fastp = fastp->next->next;
		}
	}
	return false;
}