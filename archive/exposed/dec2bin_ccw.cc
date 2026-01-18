void
dec2bin(int num)
{
	deque<char> bin;

	while (num > 0) {
		if ((num % 2) == 0) {
			bin.push_front("0");
		else
			bin.push_front("1");
		num /= 2;
	}
}
