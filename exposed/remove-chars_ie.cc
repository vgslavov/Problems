// O(n + m)

using namespace std;

// use unordered_map instead:
// if str and remove are short or chars have many possible values (e.g. Unicode)
string remove_chars(string str, string remove)
{
	// or 256 (for all ASCII chars)
	bool flags[128];

	for (int i = 0; i < flags.size(); i++) {
		flags[i] = false;
	}

	// TODO: verify c_str() works
	for (int i = 0; i < remove.length(); i++) {
		flags[remove[i].c_str()] = true;
	}

	int dst = 0;
	for (int src = 0; src < str.length(); src++) {
		if (flags[str[src].c_str()] == false) {
			str[dst] = str[src];
			++dst;
		}
	}
	return str;
}

string remove_chars_hash(string instr, string remove)
{
    typedef unordered_map<char, int> char2inthash;
    char2inthash remtbl;

    chart2inthash::iterator itr;
    for (int i = 0; i < remove.length(); i++) {
        itr = remtbl.find(remove[i]);
        if (itr != remtbl.end())
            itr->second += 1;
        else
            remtbl[remove[i]] = 1;
    }

    int dst = 0;
    for (int i = 0; i < instr.length(); i++) {
        if (remtbl.count(instr[i]) == 0) {
            instr[dst] = instr[i];
            ++dst;
        }
    }
    return instr;
}
