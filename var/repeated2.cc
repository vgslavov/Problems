using namespace std;

// no additional space
// - compare every char to every other char: O(n^2)
// - sort (O(n logn)), then check linearly (O(n)) every neighbor
// (may use extra space because of sorting)

// using bool array
// time: O(n), space: O(n)
// supports only ASCII values
bool is_unique-array(string instr)
{
    // ASCII only
    bool tbl[256] = { false };

    // set all
    int strlen = instr.length();
    for (int i = 0; i < strlen; i++) {
        // already seen
        if (tbl[instr[i]])
            return false;
        else
            tbl[instr[i]] = true;
    }
    return true;
}

// using a single int (bit vector)
// time: O(n), space: O(1)
// supports only strings of lower ‘a’ through ‘z’

// using a hash table
// time: O(n), space: O(n)?
// supports all values
bool is_unique-hash(string instr)
{
    typedef unordered_map<char, int> char2int;
    char2int hashtbl;

    char2int::iterator itr;
    int len = instr.length();
    for (int i = 0; i < len; i++) {
        itr = hashtbl.find(instr[i]);
        // already seen
        if (itr != hashtbl.end())
            return false;
        else
            hashtbl[instr[i]] = 1;
    }
    return true;
}
