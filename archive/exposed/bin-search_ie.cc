// O(log n)
// TEST: 0-sized, 1-sized, odd, even, exists, doesn't exist, 1st, last

using namespace std;
// wrapper
int bin_searchW(vector<int> v, int num)
{
	return bin_search(v, num, 0, v.size() - 1);
}

// recursive
int bin_search(vector<int> v, int num, int lower, int upper)
{
	int range, mid;
	
	range = upper - lower;

	// wrong range
	if (range < 0) {
		return -1;
	// base case (not found)
	// ATTN: don't forget to check if v[lower] == num!
	} else if (range == 0 && v[lower] != num) {
		return -1;
	}

	// not sorted
	if (v[lower] > v[upper])
		return -1;

	// ATTN: don't forget to add lower!
	mid = range / 2 + lower;
	// base case (found)
	if (num == v[mid]) {
		return mid;
	} else if (num < v[mid]) {
		return bin_search(v, num, lower, mid-1);
	} else {
		return bin_search(v, num, mid+1, upper);
	}
}

// iterative
int bin_searchI(vector<int> v, int num)
{
	int range, upper, lower, mid;

	lower = 0;
	upper = v.size() - 1;
	range = upper - lower;

	// wrong range (0-sized case)
	if (range < 0) {
		return -1;
	}

	// ATTN: no conditions!
	while (1) {
		range = upper - lower;

		// not found
		// ATTN: don't forget to check if v[lower] == num!
		if (range == 0 && v[lower] != num) {
			return -1;
		}

		// not sorted
		if (v[lower] > v[upper]) {
			return -1;
		}

		mid = range/2 + lower;
		if (num == v[mid]) {
			return mid;
		} else if (num < v[mid]) {
			upper = mid - 1;
		} else {
			lower = mid + 1;
		}
	}
}