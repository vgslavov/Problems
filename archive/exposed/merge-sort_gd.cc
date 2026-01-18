using namespace std;

// O(n log(n))
vector<int>
merge_sort(vector<int> v)
{
	// base case
	if (v.length() < 2)
		return v;

	// split in 2 subarrays
	int mid = v.length() / 2;
	vector<int> left (mid);
	vector<int> right (v.length() - mid);

	// copy vector (inefficient)
	// TEST: mid or mid+1
	vector<int>::iterator itr = v.begin() + mid;
	copy(v.begin(), itr, left.begin());
	++itr;
	copy(itr, v.end(), right.begin());

	// sort subarrays
	merge_sort(left);
	merge_sort(right);

	return merge(v, left, right);
}

// O(n)
vector<int>
merge(vector<int> v, vector<int> left, vector<int> right)
{
	int vi, li, ri;

	vi = li = ri = 0;

	// merge while there are elements (overwrite v)
	while (li < left.length() && ri < rigth.length()) {
		if (left[li] <= right[ri])
			v[vi++] = left[li++];
		else
			v[vi++] = right[ri++];
	}

	// copy rest of whichever array remains
	while (li < left.length()) {
		v[vi++] = left[li++];
	}
	while (ri < right.length()) {
		v[vi++] = rigth[ri++];
	}

	return v;
}