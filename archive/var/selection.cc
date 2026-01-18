// selection: using STL (O(n) time, space?), k-th element
nth_element(A.begin(), A.begin() + k - 1, A.end());

// selection: median using STL (O(n) time, space?)
nth_element(A.begin(), A.begin() + A.size()/2, A.end());

// selection: median in stream
// O(log n) time per element read in
void online_median(istringstream *sin)
{
    // max-heap: store lower half
    priority_queue<int, vector<int>, less<int> > L;

    // min-heap: store higher half
    priority_queue<int, vector<int>, greater<int> > H;

    int x;
    while (*sin >> x) {
        // put in the right heap
        // x is greater than the largest of the Lower half, put in higher half
        if (!L.empty() && x > L.top())
            H.push(x);
        // x is smaller or equal to the largest of the Lower half, put there
        else
            L.push(x);

        // make sure L and H are not off by more than one in size
        if (H.size() > L.size() + 1) {
            L.push(H.top());
            H.pop();
        } else {
            H.push(L.top());
            L.pop();
        }

        // even # of elements, calc median
        if (H.size() == L.size()) {
            cout << 0.5 * (H.top() + L.top()) << endl;
        // odd, median is in the middle
        } else {
            cout << (H.size() > L.size() ? H.top() : L.top()) << endl;
        }
    }
}

// k-th largest: min_heap, O(n logk) time, O(k) space
// assumption: sequence of elements, one at a time, length not known
void find_kth_largest_stream(istringstream *sin, int k)
{
    priority_queue<int, vector<int>, greater<int> > min_heap;

    // for first k, output min (top)
    int x;
    for (int i = 0; i < k && *sin >> x; i++) {
        min_heap.push(x);
        cout << min_heap.top() << endl;
    }

    // after k inserts in a min-heap, root holds k-th largest!

    while (*sin >> x) {
        // discard smallest (top) to make room for k-th largest
        // if x is smaller, skip it
        if (min_heap.top() < x) {
            min_heap.pop();
            min_heap.push(x);
        }
        cout << min_heap.top() << endl;
    }
}

// get top k ranks: min-heap
// time: O(n logk)
// space: O(k)
vector<float> get_topk(vector<float> ranks, int k)
{
    // min heap
    priority_queue<float, vector<float>, greater<float>> min_heap;

    for (size_t i = 0; i < k && i != ranks.size(); ++i) {
        min_heap.push(ranks[i]);
    }

    if (ranks.size() < k)
        return;

    for (size_t j = k; j != ranks.size(); ++j) {
        float top = min_heap.top();
        if (top < ranks[j]) {
            min_heap.pop();
            min_heap.push(ranks[j]);
        }
    }

    vector<float> topk(min_heap.size());

    // TODO: verify
    //copy(&(min_heap.top()), &(min_heap.top()) + min_heap.size(), &topk[0]);

    // or
    while (!min_heap.empty()) {
        topk.push_back(min_heap.top());
        min_heap.pop();
    }

    return out;
}

// k-th largest: vector and library selection, O(n)
// assumption: sequence of elements, one at a time, length not known
int find_kth_largest_stream(istringstream *sin, int k)
{
    vector<int> M;
    int x;

    while (*sin >> x) {
        M.push_back(x);

        // TODO: why 2k - 1 size?
        if (M.size() == ((k << 1) - 1)) {
            // keep k largest, discard rest
            nth_element(M.begin(), M.begin() + k - 1, M.end(), greater<int>());
            M.resize(k);
        }
    }

    nth_element(M.begin(), M.begin() + k - 1, M.end(), greater<int>());

    // return the k-th largest one
    return M[k - 1];
}
