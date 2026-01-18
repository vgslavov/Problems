using namespace std;

// string to integer: go left to right!
int str2int(string instr)
{
    bool isneg = false;
    int len = instr.length();
    int i = 0;

    if (instr.at(i) == ‘-’) {
        isneg = true;
        ++i;
    }

    if (instr == ‘-’) {
        throw invalid_argument(“illegal input”);
    }

    int num = 0;
    // process left to right!
    while (i < len) {
        // 1st!
        num *= 10;
        // then
        // digit = value of digit char - value of ‘0’
        if (!isdigit(instr[i]))
            throw invalid_argument(“illegal input”);
        num += instr[i++] - ‘0’;
    }

    if (isneg)
        num = -num;

    return num;
}

// integer to char *: go right to left!
char * int2str(int num)
{
    bool isneg = false;
    // can fit int
    int MAX_DIGITS = 10;
    // +1 for sign
    char numchar[MAX_DIGITS+1];

    if (num < 0)
        num = -num;
        isneg = true;
    }

    int i = 0;
    // process right to left!
    // use do/while in case num is 0
    do {
        // modulo to get digit
        // value of digit char = digit + value of ‘0’
        numchar[i++] = (char)((num % 10) + ‘0’);
        num /= 10;
    } while (num != 0 && i < MAX_DIGITS+1);

    if (isneg)
        numchar[i] = ‘-’;

    // reverse string in-place
    int start = numchar[0];
    int end = numchar[i];
    int tmp;
    while (start < end) {
        tmp = numchar[end];
        numchar[end--] = numchar[start];
        numchar[start++] = tmp;
    }
    return numchar;
}

// summary: left to right
int str2int(const string &str)
{
    bool is_neg = s[0] == ‘-’;
    int res = 0;

    for (int i = is_neg; i != str.size(); ++i) {
        int digit = str[i] - ‘0’;
        res = res * 10 + digit;
    }

    return is_neg ? -res : res;
}

// summary: right to left, then reverse
// insights:
// - least significant digit (rightmost) is equal to ‘x mod 10’
// - rest are x/10
string int2str(int num)
{
    bool isneg = false;

    if (num < 0) {
        isneg = true;
        num = -num;
    }

    string s;
    // right to left, then reverse
    while (num) {
        s.push_back(num % 10 + ‘0’);
        num /= 10;
    }

    if (s.empty())
        return “0”;

    if (isneg)
        s.push_back(‘-’);

    reverse(s.begin(), send());
    return s;
}
