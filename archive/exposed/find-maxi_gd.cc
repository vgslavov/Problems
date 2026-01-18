using namespace std;

// sort (mergesort | heapsort): O(n log(n)) + O(i) = O(n log(n))
int
find_maxi_sort(vector<int> v, int i)
{

}

// build heap: O(n) + i * extract max: O(i log(n)) = O(n + i log(n))
int
find_maxi_heap(vector<int> v, int i)
{

}

// O(n)
int
find_max2(vector<int> v)
{
	int max1, max2;

	if (v.at(0) > v.at(1)) {
		max1 = v.at(0);
		max2 = v.at(1);
	} else {
		max1 = v.at(1);
		max2 = v.at(0);
	}

	for (int i = 2; i < v.length(); i++) {
		if (v[i] > max1) {
			max2 = max1;
			max1 = v[i];
		} else if {v[i] > max2) {
			max2 = v[i];
		}
	}
	return max2;
}

// Select algorithm from CLRS: O(n)
int
find_maxi_select(vector<int> v, int i)
{
	// TODO: implement
}