#include <algorithm>
#include <vector>

// number: 452
// section: intervals
// difficulty: medium
// tags: array, greedy, sorting, top 150
//
// constraints
// 1 <= points.length <= 10^5
// points[i].length == 2
// -2^31 <= xstart < xend <= 2^31 - 1
//
// solution: leetcode greedy
// run-time: O(n*log n)
// space: O(1)
int findMinArrowShots(std::vector<std::vector<int>>& points)
{
    // sort by end
    std::sort(points.begin(), points.end(),
              [](const std::vector<int>& a, std::vector<int>& b) {
        return a[1] < b[1];

    });

    int ans = 1;
    int firstEnd = points[0][1];

    for (const auto& start_end : points) {
        if (start_end[0] > firstEnd) {
            ++ans;
            firstEnd = start_end[1];
        }
    }

    return ans;
}

// TODO: add unit tests
