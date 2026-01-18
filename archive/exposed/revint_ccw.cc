// example

1234

1234 % 10 = 4
1234 / 10 = 123 = num
0 * 10 + 4 = 4 = res

123 % 10 = 3
123 / 10 = 12 = num
4 * 10 + 3 = 43 = res

12 % 10 = 2
12 / 10 = 1 = num
43 * 10 + 2 = 432 = res

1 % 10 = 1
1 / 10 = 0 = num
432 * 10 + 1 = 4321 = res

int
revint(int num)
{
	int res = 0;
	int tmp;

	while (num > 0) {
		tmp = num % 10;
		num /= 10;
		res = res * 10 + tmp;
	}
	return res;
}
