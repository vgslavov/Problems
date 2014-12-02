// easy solution: use stack
void reverse_words(string s)
{

}

// general solution (inefficient, inelegant)
// TODO: confirm int str[] is modified at caller
bool reverse_words(char str[])
{
	char *buf;
	// ATTN: use integer positions rather than pointers!
	int len, readpos, writepos, begw, endw;

	// create temporary buffer
	len = strlen(str);
	// ATTN: len doesn't include '\0'
	buf = (char *)malloc(len + 1);
	if (buf == NULL) return false;

	readpos = str[len-1];
	
	while (readpos >= 0) {
		// copy non-word chars directly
		if (str[readpos--] == ' ') {
			buf[writepos++] = ' ';
		// non-word chars
		} else {
			endw = readpos;
			// find the beginning of the word
			// ATTN: check that you don't go past the beginning of the str
			while (readpos >= 0 && str[readpos] != ' ') {
				--readpos;
			}
			// go forward (readpos points to ' ')
			begw = readpos + 1;
			// copy word
			for (int i = begw; i <= endw; i++) {
				buf[writepos++] = str[begw];
				--readpos;
			}
		}
	}
	// NUL terminate buffer
	buf[len-1] = '\0';
	// copy buffer over original string
	strlcpy(str, buf, len+1);
	// ATTN: don't forget to free!
	free(buf);

	return true;
}

// elegant and more efficient (no temporary buffer)
void reverse_words_inplace(char str[])
{
	int readpos, len, begw;

	len = strlen(str);
	readpos = 0;

	// reverse the whole string
	reverse_string(str, readpos, len-1);

	while (readpos < len) {
		// skip non-word chars
		if (str[readpos] == ' ') {
			++readpos;
		} else {
			begw = readpos;
			// find end of word
			while (readpos < len && str[readpos] != ' ') {
				++readpos;
			}
			// ATTN: go back one (pointing to ' ' or end of str)
			--readpos;
			// reverse back individual words
			reverse_string(str, begw, readpos);
		}
		// ATTN: advance to next token
		++readpos;
	}
}

// in-place
void reverse_string(char str[], int start, int end)
{
	char tmp;

	// TODO: same as != ?
	while (start < end) {
		tmp = str[start];
		str[start++] = str[end];
		str[end--] = tmp;

	}
}
