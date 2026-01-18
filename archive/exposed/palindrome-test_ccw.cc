bool
is_palindrome(string s)
{
	int start = 0;
	int end = s.length() - 1;

	while (start <= end) {
		if (s.at(start) == s.at(end)) {
			++start;
			--end;
		} else
			return false;
	}
	return true;
}
