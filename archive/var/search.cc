// middle element calculation
// TODO: memorize
// both r and l > 0
int m1 = l + ((r - l) >> 1);
// r > 0, l < 0
int m2 = ((l + r) >> 1);

// binary: iterative, O(log n)
// T(n) = T(n/2) + c
// assumptions: sorted array
int bin_search(const vector<int> &V, int k)
{
    int l = 0;
    int r = V.size() - 1;

    while (l <= r) {
        // ATTN: to prevent overflow, check the signs of r and l!
        // both l and r are positive?
        int m = l + ((r - l) >> 1);
        // r > 0, l < 0
        //int m = ((l + r) >> 1);

        // too big, discard right half
        if (V[m] > k) {
            r = m - 1;
        // found!
        } else if (V[m] == k) {
            return m;
        // V[m] < k: too small, discard left half
        } else {
            l = m + 1;
        }
    }

    // not found
    return -1;
}

// binary: recursive, O(log n)
// assumptions: sorted array
int bin_search(const vector<int> &V, int k)
{
    return bin_search_helper(V, k, 0, V.size() - 1);
}

int bin_search_helper(const vector<int> &V, int k, int l, int r)
{
    // base cases
    if (l > r)
        return -1;
    else if (l == r && V[l] != k)
        return -1;

    int m = l + ((r - l) >> 1);

    if (V[m] == k) {
        return m;
    } else if (V[m] > k) {
        return bin_search_helper(V, k, l, m - 1);
    } else {
        return bin_search_helper(V, k, m + 1, r);
    }
}

// binary search solution
// O(n logn) time (sort+bin_search), O(n) space
int find_k_complement_bsearch(int K, const vector<int> &A)
{
    vector<int> B = A;
    int kcount = 0;
    int n = B.size();

    sort(B.begin(), B.end());

    for (int i = 0; i < n; i++) {
        int diff = K - A[i];
        if (binary_search(B.begin(), B.end(), diff))
            ++kcount;
    }

    return kcount;
}

// hash map solution
// O(n) time, O(m) space
// (m is the # of unique ints in A)
int find_k_complement_map(int K, const vector<int> &A)
{
    unordered_map<int, long long> intcount;
    int n = A.size();

    for (int i = 0; i < n; i++) {
        intcount[A[i]] += 1;
    }

    int kcount = 0;
    for (int i = 0; i < n; i++) {
        if (intcount.count(K - A[i]))
            ++kcount;
    }

    return kcount;
}

// binary: 1st occurrence of k, O(log n)
// assumptions: sorted array
int search_first(const vector<int> &V, int k)
{
    int l = 0;
    int r = V.size();
    int res = -1;

    while (l <= r) {
        int m = l + ((r - l) >> 1);

        if (V[m] > k) {
            r = m - 1;
        } else if (V[m] == k) {
            // record found element idx, but keep searching to the left!
            res = m;
            r = m - 1;
        } else {
            l = m + 1;
        }
    }

    return res;
}

// binary: 1st element greater than k, O(log n)
// assumptions: sorted array
int search_first_larger_k(const vector<int> &V, int k)
{
    int l = 0;
    int r = V.size() - 1;
    int res = -1;

    while (l <= r) {
        int m = l + ((r - l) >> 1);

        if (V[m] > k) {
            // record greater element idx, but keep searching to the left
            res = m;
            r = m - 1;
        // discard left half
        } else {
            l = m + 1;
        }
    }

    return res;
}

// binary: V[i] = i, O(log n)
// assumptions: sorted array with distinct elements
int search_index_value_equal(const vector<int> &V)
{
    int l = 0;
    int r = V.size() - 1;

    while (l <= r) {
        int m = l + ((r - l) >> 1);

        // V[m] = m + 0
        int val = V[m] - m;

        // found if 0 = V[m] - m;
        if (val == 0) {
            return m;
        } else if (val > 0) {
            r = m - 1;
        } else {
            l = m + 1;
        }
    }

    return -1;
}

// binary: smallest element, O(log n)
// assumptions: cyclically sorted array with distinct elements
// if repeated elements, O(n)
// TODO: understand better
int search_smallest(vector<int> &V)
{
    int l = 0;
    int r = V.size() - 1;

    // ATTN: don’t check equal!
    while (l < r) {
        int m = l + ((r - l) >> 2);

        // discard left half because values will decrease on right
        if (V[m] > V[r]) {
            l = m + 1;
        // V[m] <= V[r], discard right half, values will decrease on left
        } else {
            r = m;
        }
    }

    // l == r
    return l;
}

// binary: uknown length, O(log n)
// TODO: understand better why these values for range
int search_uknown_len(const vector<int> &V, int k)
{
    int p = 0;

    // look for end and k (range where it exists) at the same time:
    // examine V[2^p - 1]
    // TODO: why?
    while (true) {
        try {
            // use .at()!
            int val = V.at((1 << p) - 1);

            // found!
            if (val == k) {
                return (1 << p) - 1;
            // went too far to the right
            } else if (val > k) {
                break;
            }
        // out of boundary, stop searching for end
        } catch (const exception& e) {
            break;
        }
        ++p;
    }

    // binary search b/w V[2^(p - 1)] and V[2^p - 2]
    // TODO: why?
    int l = 1 << (p - 1);
    int r = (1 << p) - 2;
    while (l <= r) {
        int m = l + ((r - l) >> 1);
        try {
            int val = V.at(m);

            // found!
            if (val == m) {
                return m;
            } else if (val > k) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        // out of bounary, search on left
        } catch (const exception& e) {
            r = m - 1;
        }
    }

    // not found
    return -1;
}

// binary: square root, O(log x)
// TODO: understand compare() from EPI for eps precision
double square_root(double x)
{
    double l, r;

    // tighten bounds based on value of x!
    if (x < 1.0) {
        l = x;
        r = 1.0;
    // x >= 1.0
    } else {
        l = 1.0;
        r = x;
    }

    // or use
    // l = 0;
    // r = numeric_limits<float>::max();

    while (l < r) {
        double m = l + 0.5 * (r - l);
        double square_m = m * m;

        if (square_m == x) {
            return m;
        } else if (square_m > x) {
            r = m;
        } else {
            l = m;
        }
    }

    return l;
}

// binary: matrix, O(log n)
// assumption: rows and columns are sorted in increasing order
bool matrix_search(const vector<vector<int> > &V, int x)
{
    // first row
    int r = 0;
    // last column
    int c = V[0].size() - 1;

    // move from upper right, to lower left corner of the matrix
    while (r < V.size() && c  >= 0) {
        if (V[r][c] == x) {
            return true;
        // x is greater than all elements in row r, go to next row
        } else if (V[r][c] < x) {
            ++r;
        // V[r][c] > x
        // x is smaller than all elements in column c, go to previous column
        } else {
            --c;
        }
    }

    return false;
}

// binary: min and max simultaneously with fewer comparisons, ceil(3n/2) - 2
// assumption: sorted array
pair<int, int> find_min_max(const vector<int> &V)
{
    // n = 1
    if (V.size() <= 1)
        return { V.front(), V.front() };

    // init min and max (minmax() in <algorithm>)
    pair<int, int> min_max = minmax(V[0], V[1]);

    // process 2 items at a time (3 comparisons for each pair)
    // ATTN: i + 1!
    for (int i = 2; i + 1 < V.size(); i += 2) {
        pair<int, int> local_pair = minmax(V[i], V[i+1]);
        min_max = { min(min_max.first, local_pair.first),
                     max(min_max.second, local_pair.second) };
    }

    // if V.size() is odd, one element left
    if (V.size() & 1) {
        min_max = { min(min_max.first, V.back()), max(min_max.second, V.back()) };
    }

    return min_max;
}
