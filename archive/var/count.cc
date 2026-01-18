// words
int count_words(const char *str)
{
    bool in_word = false;
    int nwords = 0;
    const char *p = str;

    // check for *p, not p!
    while (*p) {
        // start of new word
        if (!in_word && isalpha(*p)) {
            in_word = true;
            ++nwords;
        // start of spaces
        } else if (in_word && *p == ‘ ‘) {
            in_word = false;
        }
        ++p;
    }
    return nwords;
}

// bits: 3. shift mask (best O(n), always go through all n bits of int)
int count_bits(int num)
{
    unsigned int mask = 1;
    unsigned int newnum = num;
    int mbits = 0;

    while (mask != 0) {
        if ((newnum & mask) == 1)
            ++mbits;
        mask = mask << 1;
    }
    return mbits;
}

// bits: 2. shift num (worst O(n), but can stop sooner, after all m 1 bits fall off)
int count_bits(int num)
{
    unsigned int mask = 1;
    unsigned int newnum = num;
    int mbits = 0;

    while (newnum != 0) {
        if ((newnum & mask) == 1)
            ++mbits;
        newnum = newnum >> 1;
    }
    return mbits;
}

// parity: shift num (worst O(n))
// parity is 1 if # of bits is odd, 0 otherwise (even)
short parity(unsigned long num)
{
    short result = 0;

    while (num) {
        // XOR: even 1 bits will cancel out (=0), odd will leave 1
        result ^= (num & 1);
        num >>= 1;
    }
    return result;
}

// bits: 1. turn off right-most bit (worst O(m), where m is # of 1 bits)
int count_bits(int num)
{
    int mbits = 0;

    while (num != 0) {
        num = num & (num - 1);
        ++mbits;
    }
    return mbits;
}

// parity: turn off right-most bit (worst O(m))
short parity(unsigned long num)
{
    short result = 0;

    while (num) {
        // # of XORs == # of set bits
        result ^= 1;
        // drop lowest (rigth-most) set bit
        num &= (num - 1);
    }
    return result;
}

// TODO: bits: 0. parallel approach (O(log n))
