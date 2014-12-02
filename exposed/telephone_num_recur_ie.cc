// TODO: test manually and understand
// O(3^n)

using namespace std;

// recursive
class TelephoneNumber {
	public:
		TelephoneNumber(vector<int> n);
		void printWords();
	private:
		void printWords(int curDigit);
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
	printWords(0);
}

void
TelephoneNumber::printWords(int curDigit)
{
	// base case?
	if (curDigit == PHONE_NUM_LEN) {
		// TODO: can you print vectors like this?
		cout << result << endl;
		// TODO: clear result?
		return;
	}
	// move left to right
	for (int i = 1; i <= 3; i++) {
		// TODO: replace with push_back()?
		//result.push_back(getCharKey(phoneNum[curDigit], i));
		result[curDigit] = getCharKey(phoneNum[curDigit], i);
		printWords(curDigit + 1);
		if (phoneNum[curDigit] == 0 || phoneNum[curDigit] == 1)
			return;
	}
}

// TODO: implement
char
TelephoneNumber::getCharKey(inte telephoneKey, int place)
{
	return 'n';
}