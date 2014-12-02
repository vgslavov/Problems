// TEST: 0, -1
// O(n)

int
count_ones(int num)
{
	int n = 0;
	// use unsigned int to prevent C++ from add 1s insted of 0s when >>
	// (or cast to unsigned int)
	unsigned int newnum = num;

	// don't check all the bits if newnum becomes 0
	while (newnum != 0) {
		if ((newnum & 1) == 1)
			++n;

		// shift right 1 bit to divide (/) by 2
		// (iterates through all the bits so we can use the same mask (1)
		newnum = newnum >> 1;
	}

	return n;
}