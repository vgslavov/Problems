// O(n)

using namespace std;

char
first_nonrepeated(string str)
{
	unordered_map<char, int> hashmap;
	unordered_map<char, int>::iterator itr;

	// build hash map with character counts
	for (int i = 0; i < str.length(); i++) {
		itr = hashmap.find(str[i]);
		if (itr != hashmap.end())
			itr->second += 1;
		else
			hashmap[str[i]] = 1;
	}

	// don't go through hashmap, go through string (hashmap is unordered)
	for (int i = 0; i < str.length(); i++) {
		itr = hashmap.find(str[i]);
		if ((itr != hashmap.end()) && (itr->second == 1)) {
			return str[i];
		}
	}
	return NULL;
}