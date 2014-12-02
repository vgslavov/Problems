// TEST: 2-element array, identical elements

using namespace std;

void
quicksort_opt(vector<int> &v)
{
	// TODO: why len - 1?
	quicksort_opt(v, 0, v.length() - 1);
}

void
quicksort_opt(vector<int> &v, int left, int right)
{
	int pivot = v[(left + right)/ 2];
	int i = left;
	int j = right;

	while (i <= j) {
		// find value in left part. to swap
		while (data[i] < pivot) i++;

		// find value in right part. to swap
		// ATTN: go back!
		while (data[j] > pivot) j--;

		// swap if in wrong order
		if (i <= j) {
			swap(v, i, j);
			++i;
			--j;
		}
	}

	// apply recursively until the partitions are empty
	if (left < j)
		quicksort_opt(v, left, j);

	if (i < right)
		quicksort_opt(v, i, right);
}

void
quicksort_swap(vector<int> &v)
{
	quicksort_swap(v, 0, v.length());
}

void
quicksort_swap(vector<int> &v, int start, int len)
{
	if (len < 2) return;

	// ATTN: pivot and end pos are relative to start!
	int pivotpos = start + len / 2;
	// ATTN: save pivot value (because of swapping)!
	int pivot = v[pivotpos];
	int endpos = start + len;
	int curpos = start;

	// ATTN: swap pivot to end (test case: identical elements)
	// TODO: or --endpos?
	swap(v, pivotpos, endpos--);

	// partition
	while (curpos < endpos) {
		if (v[curpos] > pivot)
			// TODO: or --endpos?
			swap(v, curpos, endpos--);
		else
			++curpos;
	}

	// ATTN: swap pivot back to original position!
	swap(v, end, start + len - 1);

	// ATTN: calculate size of partitions (endpos points to middle now)
	int llen = endpos - start;
	int rlen = len - llen - 1;

	if (llen > 1)
		quicksort_swap(v, start, llen);
	if (rlen > 1)
		quicksort_swap(v, end + 1, rlen);
}

// O(1)
void
swap(vector<int> &v, int pos1, int pos2)
{
	int tmp;

	while (pos1 != pos2) {
		tmp = v[pos1];
		v[pos1] = v[pos2];
		v[pos2] = tmp;	
	}
}