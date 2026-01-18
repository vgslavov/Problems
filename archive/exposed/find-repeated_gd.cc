using namespace std;

// O(n)
// find only odd int in array
// find only duplicated int in array
int
find_repeated_map(vector<int> v)
{
	// or use bool array where size:
	// {28 (only letters, check flags[s[i] - 'a']), 128, 256 (all ASCII}
	//bool flags[size];
	unordered_map<int, int> hashmap;
	unordered_map<int, int>::iterator itr;

	for (int i = 0; i < vector.length(); i++) {
		itr = hashmap.find(v.at(i));
		// found
		if (itr != hashmap.end()) {
			itr->second += 1;
		} else {
			hashmap[v.at(i)] = 1;
		}
	}

	// odd
	for (itr = hashmap.begin(); itr != hashmap.end(); itr++) {
		if (itr->second % 2 != 0)
			cout << itr->first;
	}

	// duplicated
	for (itr = hashmap.begin(); itr != hashmap.end(); itr++) {
		if (itr->second == 2)
			cout << itr->first;
	}

	return -1;
}

// O(n), no additional memory
// XOR
int
find_odd_repeated_xor(vector<int> v)
{
	int k = 0;

	for (int i = 0; i < vector.length(); i++) {
		k = k ^ v[i];
	}
	return k;
}

// O(n log(n))
// sort
int
find_odd_repeated_sort(vector<int> v)
{

}

// O(n)
// find 1st nonrepeated char in a string
char
find_nonrepeated(string str)
{
	unordered_map<char, int> hashmap;
	unordered_map<char, int>::iterator itr;

	for (int i = 0; i < str.length(); i++) {
		itr = hashmap.find(str[i]);
		if (itr != hashmap.end()) {
			itr->second += 1;
		} else {
			hashmap[str[i]] = 1;
		}
	}

	// don't go through hashmap, go through string (hashmap is unordered)
	for (int i = 0; i < str.length(); i++) {
		// or check if hashmap.count(str[i]) > 0
		itr = hashmap.find(str[i]);
		if ((itr != hashmap.end()) && (itr->second == 1)) {
			cout << str[i];
		}
	}
	return NULL;
}

// hashmap
int
find_max_repeated_map(vector<int> v)
{
	int maxfreq = 0;
    int maxval = 0;
	unordered_map<int, int> hashmap;
	unordered_map<int, int>::iterator itr;

	for (int i = 0; i < v.length(); i++) {
		itr = hashmap.find(v[i]);
		if (itr != hashmap.end()) {
			itr->second += 1;
			if (itr->second > maxfreq)
                maxval = itr->first;
				maxfreq = itr->second;
		} else {
			hashmap[v.at(i)] = 1;
		}
	}
	
}

// priority queue
char
find_max_repeated_queue(string str)
{

}
