/*
- Bubblesort, Insertion Sort and Selection Sort are bad
- Shellsort is better but nowhere near the theoretical O(N log N) limit
- Quicksort:
  - great when it works, but unreliable
  - O(n^2) in worst case
- Mergesort:
  - reliably good
  - stable (carefully implemented, add index to rank keys and break ties)
  - not in-place
  - requires O(N) auxiliary space
- Heapsort:
  - reliably good
  - in-place
  - unstable
  - about a factor of 4 slower than Quicksort's best case

Best choices for:
- Array: quicksort, heapsort
- Linked-list: mergesort (worst O(N log N) time, O(1) space)
- Generic, best choice: well-implemented quicksort
- Fewer than 10: insertion sort (easy to code, asymptotically superior)
- Elements w/i k places from final loc: min-heap (O(n log k))
- Small # of distinct keys: counting sort
  - array: if max element ~ size of list
  - BST: keys are numbers, value are freqs
    - if many dup keys, linked-lists for same keys
    - in-order traversal of BST to print sorted result
*/

// compare function
// return: -1 if fist item is smaller than second, 0 if equal, and 1 otherwise
// TODO: practice comparison functions
struct Compare {
    bool operator() (const pair<int, int> &lhs, const pair<int, int> &rhs) const
    {
        return lhs.first < rhs.first;
    }
};

// sort stack: recursive
// TODO: study and understand
// space: O(n) on function call stack
// ptr to stack!
void sort(stack<int> *s)
{
    // base case is empty stack
    if (!s->empty()) {
        // remove top element
        int e = s->top();
        s->pop();

        // sort the rest recursively
        sort(s);

        // insert element in right place
        insert(s, e);
    }
}

void insert(stack<int> *s, int e)
{
    // base case is empty stack
    // stack is empty or already sorted
    if (s->empty() || s->top() <= e) {
        s->push(e);
    } else {
        // remove top element which is > e
        int f = s->top();
        s->pop();

        // insert e recursively
        insert(s, e);

        // put f on top
        s->push(f);
    }
}

// approximat sort (at most k positions away from sorted): min-heap
// O(?) time, O(k) space
void approximate_sort(istringstream *sin, int k)
{
    // keep k+1 numbers in memory
    priority_queue<int, vector<int>, greater<int> > min_heap;

    // put k elements in heap
    int x;
    for (int i = 0; i < k && *sin >> x; i++) {
        min_heap.push(x);
    }

    // extract min for every new num
    while (*sin >> x) {
        min_heap.push(x);
        cout << min_heap.top() << endl;
        min_heap.pop();
    }

    // extract remaining elements
    while (!min_heap.empty()) {
        cout << min_heap.top() << endl;
        min_heap.pop();
    }
}

// intersection w/o duplicates: brute-force (loop join)
// O(mn) time, O(1) space (if printing)
// assumptions: don’t have to be sorted!
vector<int> intersection1(const vector<int> &A, const vector<int> &B)
{
    vector<int> inter;

    // go over all the elements of A
    for (int i = 0; i < A.size(); i++) {
        // process only if not duplicate
        if (i == 0 || A[i] != A[i-1]) {
            // go over all the elements of B
            for (int j = 0; j < B.size(); j++) {
                if (A[i] == B[j]) {
                    inter.push_back(A[i])
                    // ATTN: stop, no sense in looking for more
                    break;
                }
            }
        }
    }

    return inter;
}

// intersection w/o duplicates: binary search
// O(n logm) time, O(1) space
// assumptions: sorted arrays
// best solution for n << m (m log(n) >> n log(m))
vector<int> intersection2(const vector<int> &A, const vector<int> &B)
{
    vector<int> inter;

    // A.size() == n (smaller)
    for (int i = 0; i < A.size(); i++) {
        // cbegin, cend: const iterators
        if (i == 0 || A[i] != A[i-1] && binary_search(B.cbegin(), B.cend(), A[i]))
            inter.push_back(A[i]);
    }

    return inter;
}

// intersection w/o duplicates: iterate in tandem
// O(m + n) time, O(1) space
// assumptions: sorted arrays
// best solution for n ~ m
vector<int> intersection3(const vector<int> &A, const vector<int> &B)
{
    vector<int> inter;
    int i = 0;
    int j = 0;

    while (i < A.size() && j < B.size()) {
        if (A[i] == B[j] && (i == 0 || A[i] != A[i-1])) {
            inter.push_back(A[i]);
            ++i;
            ++j;
        // skip smaller elements in A
        } else if (A[i] < B[j]) {
            ++i;
        // skip smaller elements in B
        } else {
            ++j;
        }
    }

    return inter;
}

// intersection w/o duplicates: hash table
// expected O(m + n) time, O(n) space
// assumptions: don’t have to be sorted!, n << m
// duplicate check doesn’t work if not sorted?
vector<int> intersection4(const vector<int> &A, const vector<int> &B)
{
    vector<int> inter;
    // set (not map) is enough
    unordered_set<int> hasha;

    // A.size() == n (smaller)
    for (int i = 0; i < A.size(); i++) {
        hasha.insert(A[i]);
    }

    // B.size() == m (larger)
    for (int i = 0; i < B.size(); i++) {
        // do check for duplicates here instead of in A
        if ((hasha.find(B[i]) != hasha.end()) && (i == 0 || B[i] != B[i-1]))
            inter.push_back(B[i]);
    }

    return inter;
}

// count occurrences: sort
void count_occurrences(string S)
{
    sort(S.begin(), S.end());

    int count = 1;
    // start from 2nd so you can compare to 1st
    for (int i = 1; i < S.size(); i++) {
        // duplicate
        if (S[i] == S[i-1]) {
            ++count;
        // new char, write previous
        } else {
            cout << “(“ << S[i-1] << “, “ << count << “), ”;
            count = 1;
        }
    }

    // don’t forget last one
    cout << “(“ << S.back() << “, “ << count << “)” << endl;
}

// count occurrences:
// - aux. integer array for counting (ASCII only) + radix sort
// - BST (keys are chars, values are freqs)
// - hash table (keys are chars, values are freqs)

// remove duplicates:
// sort, O(n logn) + in-place (better cache perf.) duplicate removal, O(n), O(1) space?
void remove_duplicates(vector<int> *A)
{
    sort(A.begin(), A.end());

    // A is a ptr!
    // distance: calc. # of elements b/w 2 iterators
    // unique: remove adjacent duplicates and returns itr to the last el. not removed
    // resize: restrict A to distinct elements
    A->resize(distance(A->begin(), unique(A.begin(), A.end())));
}

// remove duplicates:
// hash table (set: key w/o value), O(n) time, O(n) space
// counting sort (if few distinct elements and n very large), O(n) time?, O(d) space

// optimum task assignment:
// given an array of sorted task durations to be completed 2 at-a-time
// assumptions: A.size() is even, A is sorted
vector<pair<int, int> > task_assignment(vector<int> A)
{
    sort(A.begin(), A.end());

    vector<pair<int, int> > P;
    for (int i = 0, int j = A.size() - 1; i < j; i++, j--) {
        P.push_back(A[i], A[j]);
    }

    return P;
}

// pair of indices that sum up to k, O(n) time, O(1) space
// assumptions: A is sorted
bool has_2_sum(const vector<int> &A, int k)
{
    int l = 0;
    int r = A.size() - 1;

    while (l <= r) {
        if (A[l] + A[r] == k) {
            return true;
        // too small, inc. idx pointing to smaller el.
        } else (A[l] + A[r] < k) {
            ++l;
        // too large, dec. idx pointing to larger. el.
        } else {
            --r;
        }
    }

    return false;
}

// 3 indices that sum up to k, sort O(n logn) + O(n) = O(n^2) time, O(1) space
bool has_3_sum(vector<int> A, int k)
{
    sort(A.begin(), A.end());

    for (int i = 0; i < A.size(); i++) {
        // sum of 2 indices in A == k - A[i]
        if (has_2_sum(A, k - A[i])) {
            return true;
        }
    }

    return false;
}

// 3 indices that sum up to k, hash table (find k-x in table), O(n) time, O(n) space
// 3 indices that sum up to k, binary search (sorted, find k-A[i]), O(n logn) time, O(1) space
