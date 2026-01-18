// TODO: test manually and understand

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Combinations {
	public:
		Combinations(string str);
		void combine();
	private:
		void combine(int start);
		string in;
		string out;
		int ncomb;
};

Combinations::Combinations(string str)
{
	ncomb = 1;
	in = str;
	out.clear();
}

void
Combinations::combine()
{
	combine(0);
}

void
Combinations::combine(int start)
{
	// optimization: exclude last input string char
	for (int i = start; i < in.length() - 1; i++) {
		out.push_back(in[i]);
		cout << ncomb++ << ": " << out << endl;
		combine(i + 1);
		out.resize(out.size() - 1);
	}
	// optimization using loop partitioning
	out.push_back(in[in.length() - 1]);
	cout << ncomb++ << ": " << out << endl;
	out.resize(out.size() - 1);
}

int
main()
{
	string mystr = "wxyz";
	Combinations *p = new Combinations(mystr);

	p->combine();
	return 0;
}