// heap: a complete binary tree
// insertions: O(log n)
// max/min: O(1)
// max/min extract: O(log n)
// search: O(n)

// left child of i: 2i + 1
// right child of i: 2i + 2

// anything that can be done with a heap, can be done with a balanced BST:
// with the same or better time & space complexity,
// but with possible implementation overhead

// find top k: use min-heap and vice versa?
// find 'closest' k: use max-heap?

// min-heap: smallest is last in array?
struct Compare {
    bool operator() (const pair<int, int>& lhs, const pair<int, int>& rhs) const
    {
        return lhs.first > rhs.first;
    }
};

// min-heap: simple data types
priority_queue<int, vector<int>, greater<int> > min_heap;

// max-heap: largest is last in array?
// priority_queue is max-heap by default (but overload Compare for pairs!)
struct Compare {
    bool operator() (const pair<int, int> &lsh, const pair<int, int> &rhs) const
    {
        lhs.first < rhs.first;
    }
};

// max-heap (by default): simple data types
priority_queue<int, vector<int> > max_heap;
