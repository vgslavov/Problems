// Twitter pre-screening

// hash map solution: O(n) time, O(m) space
// (m is the # of unique ints in A)
#include <map>
int solution(int K, const vector<int> &A) {
    map<int, long long> intcount;
    int n = A.size();
    int kcount = 0;

    // have to init to 0?
    for (int i = 0; i < n; i++) {
        intcount[A[i]] += 1;
    }

    for (int i = 0; i < n; i++) {
        kcount += intcount[K - A[i]];
    }

    return kcount;
}

// binary search solution: O(n logn) time (sort+bin_search), O(n) space
#include <algorithm>
int solution(int K, const vector<int> &A) {
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

// ?%
// pointer solution: O(n logn) time (sort+iterate), O(n) space
int solution(int K, const vector<int> &A) {
    vector<int> B = A;
    int count = 0;
    int n = B.size();
    int l = 0;
    int r = n - 1;
    
    sort(B.begin(), B.end());
    
    while (l <= r) {
        int sum = B[l] + B[r];

        if (sum == K) {
            // add one more for reverse order
            if (l != r) {
                count += 2;
            // element with itself
            } else {
                ++count;
            }

            // don't advance if duplicates which add up to K
            if (B[l] == B[l+1] || B[r] == B[r-1]) {
                // TODO
                /*
                while (B[l] + B[r] == sum) {
                    ++count;
                    ++l;
                }
                */
            // advance
            } else {
                ++l;
                --r;
            }
        } else if (sum > K) {
            --l;
        } else {
            ++r;
        }
    }

    return count;
}

// submitted
#include <algorithm>
int bin_search(int K, vector<int> B);

int solution(int K, const vector<int> &A) {
    vector<int> B = A;
    
    sort(B.begin(), B.end());
    
    return bin_search(K, B);
}

int bin_search(int K, vector<int> B) {
    int l = 0;
    int r = B.size() -1;
    int count = 0;
    
    while (l <= r) {
        int m = l + ((r -l) >> 1);
        
        int val = K - B[m];
        
        if (val == 0)
            ++count;
        else if (val > 0)
            r = m - 1;
        else
            l = m + 1;
    }
    
    return count;
}
