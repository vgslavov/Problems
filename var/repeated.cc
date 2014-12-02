// all elements twice, one element once
// only odd int in array
// only duplicate int in array
// 1st non-repeated char in string

// hash table, O(n) time, O(n) space

// XOR: elements appearing even # of times will cancel out (x^x=0), O(n) time, O(1) space

// sort, O(n logn) time

// priority queue (heap)

// majority search: find majority element (string repeated the most),
// O(n) time, O(1) space
// assumptions: single pass over a very long stream of seq. of words, majority element exists
// TODO: understand better
// if candidate appears 5 times in a row, it will take 5 diff. words to reset candidate to new
string majority_search(istringstream *sin)
{
    string candidate;
    string buf;
    int count = 0;

    // process stream in pairs: current el. and prev. most common (candidate)
    // discard 2 distinct elements
    while (*sin >> buf) {
        // record new candidate, increase counter
        if (count == 0) {
            candidate = buf;
            count = 1;
        // same word as previous candidate, increase counter
        } else if (candidate == buf) {
            ++count;
        // counter is positive, but word is different than candidate
        } else {
            --count;
        }
    }

    // left with majority element
    return candidate;
}

// hash table: distance of any closest pair of equal entries,
// O(n) time, O(d) space (d: # of distinct strings in array)
int find_nearest_repetition(const vector<string> &s)
{
    // store string and its location in array
    unordered_map<string, int> string_to_loc;

    int closest_dis = numeric_limits<int>::max();

    for (int i = 0; i < s.size(); i++) {
        if (string_to_loc.find(s[i]) != string_to_loc.end()) {
            // calc. distance to prev. occurrence and compare to min
            closest_dis = min(closest_dis, i - string_to_loc[s[i]])
        // record new string in hash table with its location
} else {
    string_to_loc[s[i]] = i;
}
    }

    return closest_dis;
}

// hash table: can letter L be written using chars from magazine M?
// n_m: # of chars in M
// c_l: # of distinct chars in L
// O(n_m) time
// O(c_l) space
// assumptions: M.size() >= L.size(), not only ASCII
bool anonymous_letter_map(const string &L, const string &M)
{
    unordered_map<char, int> hash;
    int Llen = L.size();
    int Mlen = M.size();

    // put all chars from L into hash and calc. freq.
    for (int i = 0; i < Llen; i++) {
        ++hash[L[i]];
    }

    for (int i = 0; i < Mlen; i++) {
        if (hash.find(M[i]) != hash.end()) {
            if (--hash[M[i]] == 0) {
                hash.erase(M[i]);

                // stop if hash is empty already
                if (hash.empty())
                    return false;
            }
        }
    }

    // if all chars in hash/L were found in M, hash will be empty
    return hash.empty();
}

// int array: can letter L be written using chars from magazine M?
// O(n + m) time?, 256 bytes
// assumptions:  M.size() >= L.size(), ASCII only
// TODO
bool anonymous_letter_array(const string &L, const string &M)
{
    int letters[256];
    // init: letters[j] = 0;
    ++letters[s[i]];
    // or
    ++letters[s[i].c_str()];
}
