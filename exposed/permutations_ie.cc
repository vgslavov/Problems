// TODO: test manually and understand
// O(n!)?

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Permutations {
	public:
		Permutations(string str);
		void permute();
	private:
		vector<bool> used;
		// TODO: or stringstream instead?
		string out;
		// TODO: const?
		string in;
		int nperm;
};

Permutations::Permutations(string str)
{
	nperm = 1;
	in = str;
	out.clear();
	// ATTN: init vector!
	for (int i = 0; i < in.length(); i++) {
		used.push_back(false);
	}
}

void
Permutations::permute()
{
	// base case
	if (out.length() == in.length()) {
		cout << nperm++ << ": " << out << endl;
		return;
	}
	for (int i = 0; i < in.length(); i++) {
		if (used[i] == true)
			continue;
		out.push_back(in[i]);
		used[i] = true;
		permute();
		used[i] = false;
		// delete appended char
		out.resize(out.size() - 1);
	}
}

int
main()
{
	string mystr = "abcd";
	Permutations *p = new Permutations(mystr);

	p->permute();
	return 0;
}