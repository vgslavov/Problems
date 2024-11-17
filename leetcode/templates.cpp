#include <algorithm>
#include <iterator>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

// Two pointers: one input, opposite ends
int fn(const std::vector<int>& v)
{
    int ans = 0;
    int left = 0;
    int right = v.size()-1;

    while (left < right) {
        if (CONDITION) {
            ++left;
        } else {
            --right;
        }
    }

    return ans;
}

// Two pointers: two inputs, exhaust both
int fn(const std::vector<int>& v1, const std::vector<int>& v2)
{
    int i = 0;
    int j = 0;
    int ans = 0;

    while (i < v1.size() && j < v2.size()) {
        // do some logic here
        if (CONDITION) {
            ++i;
        } else {
            ++j;
        }
    }

    while (i < v1.size()) {
        // do logic
        ++i;
    }

    while (j < v2.size()) {
        // do logic
        ++j;
    }

    return ans;
}

// Sliding window
int fn(const std::vector<int>& v)
{
    int ans = 0;
    int left = 0;
    int curr = 0;

    for (int right = 0; right != v.size(); ++right) {
        // do logic here to add v[right] to curr

        while (WINDOW_CONDITION_BROKEN) {
            // remove v[left] from curr
            ++left;
        }

        // update ans

    }

    return ans;
}

// Sliding *fixed* window
int fn(const std::vector<int>& v, int k)
{
    int ans = 0;
    int curr = 0;

    for (int i = 0; i < v.size() && i < k; ++i) {
        // do logic here to add v[i] to curr
    }

    // update ans

    for (int i = 0; i < std::min(k, v.size()) ; ++i) {
        // add v[i] & remove v[i-k] from curr

        // update ans

    }

    return ans;
}

// Build a prefix sum
std::vector<int> fn(const std::vector<int>& v)
{
    std::vector<int> prefix{v[0]};

    for (int i = 1; i != v.size(); ++i) {
        prefix.push_back(prefix[i-1] + v[i]);
    }

    return prefix;
}

// Efficient string building
// v is a list of chars
std::string fn(const std::vector<std::string>& v)
{
    std::string s(v.begin(), v.end());
    return s;
}
