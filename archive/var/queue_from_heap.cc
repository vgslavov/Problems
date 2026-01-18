priority_queue<pair<int, int>, vector<pair<int, int> >, Compare> max_heap;

// for max-heap when using pair<>
struct Compare {
    bool operator() (const pair<int, int> &lhs, const pair<int, int> &rhs) const
    {
        return lhs.first < rhs.first;
    }
};

// queue: max-heap
// p.first: order_ (0 to -n), p.second: element
// dequeue(): get element with max (highest neg. # or 0) order_ (first pushed)
// enqueue(): push element and order_--
