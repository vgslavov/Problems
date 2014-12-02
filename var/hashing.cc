// good hash functions

// lookup: O(1) (on avg O(1 + n/m))
// n: # of obj
// m: len of array
// load: n/m (if large, rehash)
// rehashing: O(n+m) (expensive but infrequent)

// strings
// TODO: understnd better
int string_hash(const string &str, int modulus)
{
    // large prime
    const in kMult = 997;
    int val = 0;

    for (int i = 0; i < str.size(); i++) {
        val = (val * kMult + str[i]) % modulus;
    }

    return val;
}
