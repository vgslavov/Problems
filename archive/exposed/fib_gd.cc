// TEST: -1, 0, 1, 2, 3, 4, 5
// recursive
int
fib(int n, vector<int> &v)
{
	if (n == 0) {
		// f(0) = 0
		v.push_back(0);
		return 0;
	} else if (n == 1) {
		// f(1) = 1
		v.push_back(1);
		return 1;
	} else if (n > 1) {
		// fib(n) = fib(n-1) + fib(n-2)
		int fibn = fib(n-1) + fib(n-2);
		v.push_back(fibn);
		return fibn;
	} else {
		return -1;
	}
}

// iterative
int
fib_itr(int n, vector<int> &v)
{
	if (n < 0)
		return -1;

	if (n == 0) {
		v.push_back(0);
		return 0;
	}

	int x = 1, y = 1;
	// ATTN: start at 3!
	for (int i = 3; i <= n; i++) {
		int z = x + y;
		v.push_back(z);
		x = y;
		y = z;
	}
	// TODO: why y?
	return y;
}