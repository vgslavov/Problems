#include <algorithm>
#include <vector>

// tags: two pointers
// leetcode: 11

// solution: two pointers, opposite direction
// complexity:
// run-time: O(n)
// space: O(1)
int maxArea(const std::vector<int>& v)
{
    int left = 0;
    int right = v.size()-1;
    int maxArea = 0;

    while (left < right) {
        int area = std::min(v[left], v[right]) * (right-left);
        maxArea = std::max(area, maxArea);

        // advance shorter line!
        if (v[left] < v[right]) {
            ++left;
        } else {
            --right;
        }
    }

    return maxArea;
}