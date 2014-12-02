// order of efficiency: 3 (*expected* linear time), 2 (worst), 1 (worst)
// assumption: m << n

using namespace std;

// 1.1 Sort both: O(n log(n) + m log(m)) + one pass over bigger: O(max(n, m)) = 
// O(n log(n) + m log(m) + max(n, m))
// or?
// 1.2 Sort both: O(n log(n) + m log(m)) + one pass each: O(n) + O(m) = 
// O(n log(n) + m log(m) + n + m)
vector<int>
find_inter_sort(vector<int> a, vector<int> b)
{
	vector<int> c;
	int i,j;

	// skip if already sorted
	sort(a.begin(), a.end());
	sort(b.begin(), b.end());

	c.clear();
	i = j = 0;
	// same as set_intersection(a, b, c.begin());
	while (i < a.length() && j < b.length()) {
		if (a[i] == b[j]) {
			c.push_back(a[i]);
			++i;
			++j;
		} else if (a[i] < b[j]) {
			++i;
		} else {
			++j;
		}
	}
	return c;
}

// 2. Sort *smaller*: O(m log(m)) + binary search each n in sorted m: O(n log(m)) =
// O((n + m) log(m))
// note: (n + m) log(m) < n log(n) because n + m < 2n when m < n
// note: linear if m is const in size
vector<int>
find_inter_search(vector<int> a, vector<int> b)
{
	vector<int> c;
	int alen = a.length();
	int blen = b.length();

	c.clear();
	if (alen < blen) {
		// sort smaller
		sort(a.begin(), a.end());
		// go through larger and search for each element
		for (int i = 0; i < b.length(); i++) {
			if (b[i] == bin_search(a, b[i], 0, a.length())) {
				c.push_back(b[i]);
			}
		}
	} else {
		sort(b.begin(), b.end());
		for (int i = 0; i < a.length(); i++) {
			if (a[i] == bin_search(b, a[i], 0, b.length())) {
				c.push_back(a[i]);
			}
		}
	}
	return c;
}

// efficiency: O(log n)
// assumption: v is sorted
// type: recursive
// call: bin_search(v, num, 0, v.length())
int
bin_search(vector<int> v, int num, int start, int end)
{
	// not sorted
	if (v.begin() > v.end())
		return -1;

	int range = end - start;
	// base case (not found)
	// ATTN: check if range is 0 (1 element left)
	if (range == 0 && v[start] != num)
		return -1;

	// ATTN: don't divide sum by 2!
	int mid = start + range / 2;
	
	// base case (found)
	if (v[mid] == num) {
		return v[mid];
	} else if (v[mid] > num) {
		// ATTN: return; end is mid-1!
		return bin_search(v, num, start, mid-1);
	} else {
		// ATTN: return!
		return bin_search(v, num, mid+1, end);
	}
}

// 3.1 Store 1st in hashmap: O(n) + lookup 2nd in hashmap: O(m) = O(n + m)
// 3.2 Store both in a hashmap and iterate through the hashmap to look for collisions
// disadv: uses more memory
// note: *expected* linear time, not worst
// question: should size of each affect the order?
vector<int>
find_inter_hash(vector<int> a, vector<int> b)
{
	vector<int> c;
	unordered_map<int, int> hashmap;
	unordered_map<int, int>::iterator itr;

	// store 1st in hashmap
	for (int i = 0; i < a.length(); i++) {
		itr = hashmap.find(a[i]);
		if (itr != hashmap.end()) {
			itr->second += 1;
		} else {
			hashmap[a[i]] = 1;
		}
	}

	c.clear();
	// look up each element of 2nd in hashmap
	for (int i = 0; i < b.length(); i++) {
		if (hashmap.count(b[i]) > 0) {
			c.push_back(b[i]);
		}
	}
	return c;
}
