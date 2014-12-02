// number
// reverse and compare
// limitation: overflow!
bool palindrome_int(int num)
{
    // reverse_int is defined in reverse doc
    return (num == reverse_int(num));
}

// string

// longest substring

// list
bool palindrome_list(Node *L)
{
    Node *slow = L;
    Node *fast = L;

    // find middle
    while (fast) {
        fast = fast->next;
        if (fast) {
            fast = fast->next;
            slow = fast->next;
        }
    }

    // reverse 2nd half and compare front and back
    Node *rev_back = reverse_list(slow);
    while (rev_back && L) {
        if (rev_back->data != L->data) {
            return false;
        }
        rev_back = rev_back->next;
        L = L->next;
    }
    return true;
}

// anagrams: output subsets of words which are anagrams
// m: max str len
// n: # of strings in dict
// sorting keys: O(nm log m)
// (can be reduced to O(nm) using count sort if m > 100)
// inserting into hash table and printing: O(nm)
// total: O(nm log m)
void find_anagrams(const vector<string> &dict)
{
    unordered_map<string, vector<string> > anagrams;

    // go through dictionary and store all words but sort them first
    for (int i = 0; i < dict.size(); i++) {
        string word = dict[i];

        // x & y are anagrams if sort(x) = sort(y)
        sort(word.begin(), word.end());
        anagrams[word].push_back(dict[i]);
    }

    // go through hash table and output all entries with values’ sizes >= 2
    unordered_map<string, vector<string> >::iterator itr;
    for (itr = anagrams.begin(); itr != anagrams.end(); itr++) {
        if (itr->second.size() >= 2) {
            for (int i = 0; i < itr->second.size(); i++) {
                cout << itr->second[i] << ‘ ‘;
            }
            cout << endl;
        }
    }
}

// string: check if it can be permuted to a palindrome, hash table
// O(n) time, O(d) space (d: # of distinct chars in string)
bool check_permutation2palindrome(const string &s)
{
    // map chars to freqs
    unordered_map<char, int> hash;
    int len = s.size();

    // calc. freqs. of each char
    for (int i = 0; i < len; i++) {
        if (hash.find(s[i]) != end()) {
            ++hash[s[i]];
        } else {
            hash[s[i]] = 1;
        }
    }

    // go through hash and check if # of odd freq. chars <= 1
    // even-len. strings: each char is even # of times (no odd chars)
    // odd-len. strings: all but one char is even # of times (odd char is 1)
    int odd_count = 0;
    unordered_map<char, int>::iterator itr;
    for (itr = hash.begin(); itr != hash.end(); itr++) {
        // if odd, inc. odd count but break if > 1
        if (itr->second & 1 && ++odd_count > 1)
            break;
    }

    /*
    // odd length
    if ((len & 1) && (odd_count == 1)
        return true;
    // even length
    else if (!(len & 1) && (odd_count == 0)
        return true;
    else
        return false;
    */

    // brilliant!
    // a necessary condition for a palindrome
    return odd_count <= 1;
}

// XOR
// O(n) time, O(1) space
bool check_permutation2palindrome2(const string &S)
{
    long long k = 0;
    long n = S.size();

    if (n == 1)
        return 1;

    for (int i = 0; i < n; i++) {
        char ch = S[i];
        k = k ^ ch;
    }

    if (k == 0 || isalpha(k))
        return 1;
    else
        return 0;
}

// string: check if it can be permuted to a palindrome, pointers
// O(n logn) time, O(1) space
// sorting, modifes the string
