#include <algorithm>
#include <vector>

// number: 11
// section: two pointers
// difficulty: medium
// tags: array, two pointers, greedy, top 150

// constraints
// n == height.length
// 2 <= n <= 10^5
// 0 <= height[i] <= 10^4

// solution: two pointers
// complexity
// run-time: O(n)
// space: O(1)
int maxArea(const std::vector<int>& height) {
    int i = 0;
    int j = height.size()-1;
    int ans = 0;

    while (i < j) {
        int l = j-i;
        int h = std::min(height[i], height[j]);
        ans = std::max(ans, l*h);

        if (height[i] < height[j]) {
            ++i;
        } else {
            --j;
        }
    }

    return ans;
}

// TODO: add unit tests
