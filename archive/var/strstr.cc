n: length of string
m: length of substring

// boyer-moore: sublinear

// rabin-karp: O(n+m)

// brute-force: O(n * m)
char * strstr(const char *str, const char *target)
{
    // empty substring
    if (!*target)
        return str;

    // cast so ptr is not const
    char *p1 = (char *)str;
    // iterate through string
    while (*p1) {
        char *p1begin = p1;
        char *p2 = (char *)target;
        // target matches string
        while (*p1 && *p2 && *p1 == *p2) {
            ++p1;
            ++p2;
        }
        // the whole target matched
        if (!*p2)
            return p1begin;
        // try again from next character
        p1 = p1begin + 1;
    }
    // no match
    return NULL;
}

// brute-force: O(n - m + 1)
// after n-m+1 chars don’t match, the string doesn’t have enough chars for a match
char *strstr(const char *str, const char *target)
{
    // empty substring
    if (!*target)
        return str;

    char *p1 = (char *)str;
    char *p2 = (char *)target;
    char *p1adv = (char *)str;

    // advance p1adv by m chars
    while (*p2)
        ++p1adv;

    while (*p1adv) {
        char *p1begin = (char *)p1;
        p2 = (char *)target;
        while (*p1 && *p2 && *p1 == *p2) {
            ++p1;
            ++p2;
        }
        if (!*p2)
            return p1begin;
        p1 = p1begin + 1;
        ++p1adv;
    }
    return NULL;
}
