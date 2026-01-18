bool
is_little_endian()
{
	int num = 1;
	char *ptr;

	// Q: why &
	ptr = (char *) &num;

	// byte at lowest address
	// if 1, little-endian (LSB has lowest address)
	// else (0), big-endian (MSB has lowest address)
	return (*ptr);
}