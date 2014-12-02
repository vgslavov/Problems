// TEST: -1, 0, 1, 324
using namespace std;

int str2int(string str)
{
	bool isneg;
	int num, pos, len;

	neg = false;
	num = pos = 0;
	len = str.length();
	
	// check if neg
	if (str[pos] == '-') {
		isneg = true;
		++pos;
	}
	
	// ATTN: scan string from LEFT to RIGHT to save a multiplication on each iteration
	while (pos < len) {
		// place value of num increases by a factor of 10 on each new char
		num *= 10;
		// value of digit char = digit + value of '0'
		num += str[pos++] - '0';
	}

	if (isneg == true) {
		num = -num;
	}

	return num;
}

// TODO: set MAX_DIGITS limit?
string int2str(int num)
{
	bool isneg;
	string tmp, str;
	int start, end;

	// check if neg
	if (num < 0)
		isneg == true;

	str.clear();
	// ATTN: work RIGHT to LEFT && go through loop at least once (if num == 0)
	do {
		// TODO: is append() inefficient?
		// modulo to get digit, add '0' to get digit value
		// value of digit char = digit + value of '0'
		str.append((num % 10) + '0');
		// move to next place value
		num /= 10;
	} while (num != 0);
	
	if (isneg == true) {
		str.append('-');
	}

	// reverse str in-place
	start = 0;
	end = str.length() - 1;
	// TODO: check if std::string is NUL terminated?
	while (start < end) {
		tmp = str[start];
		str[start++] = str[end];
		str[end--] = tmp;
	}

	return str;
}