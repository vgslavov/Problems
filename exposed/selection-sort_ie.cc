using namespace std;

// O(n^2), in-place, not stable, # of moves: O(n)
void
selection_sort(vector<int> &data)
{
	// ATTN: stop before last element (no swapping possible)
	for (int i = 0; i < data.length() - 1; i++) {
		swap(data, i, find_minpos(data, i));
	}
}

// O(n^2), in-place, stable, # of moves: O(n^2)
// TODO: verify data.insert()
void
selection_sort_stable(vector<int> &data)
{
	vector<int>::iterator itr;

	for (itr = data.begin(); itr != data.end(); itr++) {
		data.insert(itr, itr, find_minitr(data, itr));
	}
}

// O(n^2), in-place, stable, # of moves: O(n)
// TODO: to implement
void
selection_sort_stable_llist(list &data)
{

}

// TODO: is the return iterator still valid?
vector<int>::iterator
find_minitr(vector<int> &data, vector<int>::iterator start)
{
	vector<int>::iterator min = start;
	vector<int>::iterator itr;

	for (itr = start + 1; itr != data.end(); itr++) {
		if (*itr < *min)
			min = itr;
	}
	return min
}

int
find_minpos(vector<int> &data, int start)
{
	int min = start;

	for (int i = start + 1; i < data.length(); i++) {
		if (data[min] > data[i])
			min = i;
	}
	return min;
}

// O(n)
// TODO: implement my own vector insert
void
insert(vector<int> &data, int start, int minpos)
{

}

// O(1)
void
swap(vector<int> &data, int pos1, int pos2)
{
	int tmp;

	// ATTN: don't swap if same
	if (pos1 != pos2) {
		tmp = data[pos1];
		data[pos1] = data[pos2];
		data[pos2] = tmp;
	}
}