// O(n)
// no limit on resources
vector<int>
linear_sort(vector<int> v)
{
	vector<int> sorted (v.length());

	for (int i = 0; i < sorted.length(); i++) {
		sorted[i] = 0;
	}

	for (int i = 0; i < v.length(); i++) {
		// keep track of duplicates
		sorted[v[i]] += 1;
	}

	v.clear();
	for (int i = 0; i < sorted.length(); i++) {
		while (sorted[i] > 0) {
			v.push_back(i);
			// duplicates
			sorted[i] -= 1;
		}
	}
	return v;
}
