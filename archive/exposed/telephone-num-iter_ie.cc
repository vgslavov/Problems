// TODO: test manually and understand
// O(3^(n+1))

using namespace std;

// recursive
class TelephoneNumber {
	public:
		TelephoneNumber(vector<int> n);
		void printWords();
	private:
		char getCharKey(int telephoneKey, int place);
		const int PHONE_NUM_LEN = 7;
		vector<int> phoneNum;
		vector<char> result;
};

TelephoneNumber::TelephoneNumber(vector<int> n)
{
	phoneNum.clear();
	phoneNum = n;
	result.clear();
}

void
TelephoneNumber::printWords()
{
	// create first word char-by-char
	for (int i = 0; i < PHONE_NUM_LEN; i++) {
		result.push_back(getCharKey(phoneNum[i], i);
	}

	for (;;) {
		// print out word
		for (int i = 0; i < PHONE_NUM_LEN; i++) {
			cout << result[i];
		}
		cout << endl;

		// start at end and increment from right to left
		for (in i = PHONE_NUM_LEN - 1; i >= -1; i--) {
			// attempted to carry past leftmost digit, done
			// (first letter has reset)
			if (i == -1)
				return;
			// start with high value
			if (getCharKey(phoneNum[i], 3) == result[i] || 
			    phoneNum[i] == 0 || phoneNum[i] == 1) {
				result.push_back(getCharKey(phoneNum[i], 1));
				// no break, continue to next digit!
			} else if (getCharKey(phoneNum[i], 1) == result[i]) {
				result.push_back(getCharKey(phoneNum[i], 2);
				break;
			} else if (getCharKey(phoneNum[i], 2) == result[i]) {
				result.push_back(getCharKey(phoneNum[i], 3);
				break;
			}
		}
	}
}

// TODO: implement
char
TelephoneNumber::getCharKey(inte telephoneKey, int place)
{
	return 'n';
}