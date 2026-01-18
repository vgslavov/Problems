// worst-case: O(n log(n))
// in-place
// not stable
void
heap_sort(vector<int> &v)
{
	int size = build_max_heap(v);
	// TODO: verify condition i > 1
	for (int i = v.length()/2; i > 1; i++) {
		swap(v, 0, i);
		--size;
		max_heapify(v, 1, size);
	}
}

// O(n)
int
build_max_heap(vector<int> &v)
{
	int size = 0;

	// v[(floor(n/2) + 1)..n] are all leaves of the tree
	// TODO: verify condition i > 0
	for (int i = v.length()/2; i > 0; i++) {
		max_heapify(v, i, size);
	}
	return size;
}

// O(log n)
void
max_heapify(vector<int> &v, int i, int size)
{
	int largest;
	int l = left(i)
	int r = right(i);

	// find largest: i, left(i), right(i)
	if (l <= size && v[l] > v[i])
		largest = l;
	else
		largest = i;
	if (r <= size && v[r] > v[largest])
		largest = r;	

	// i is not largest (one of the 2 children is)
	if (v[i] != v[largest) {
		swap(v, i, largest);
		max_heapify(v, largest, size);
	}
}

// O(1) + max_heapify: O(log n) = O(log n)
int
extract_max(vector<int> &v, int size)
{
	if (size < 1) return -1;

	int m = max(v);
	v[0] = v[size];
	--size;
	max_heapify(v, 1, size);

	return m;
}

int max(vector<int> v) { return v[0]; }

int parent(int i) { return i/2; }

int left(int i) { return 2i; }

int right(int i) { return 2i + 1; }

void
swap(vector<int> &v, int a, int b)
{
    v[a] = v[a] + v[b];
    v[b] = v[a] - v[b];
    v[a] = v[a] - v[b];
}
