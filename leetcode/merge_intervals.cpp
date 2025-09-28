#include <algorithm>
#include <vector>

// number: 56
// title: Merge Intervals
// url: https://leetcode.com/problems/merge-intervals/
// section: intervals
// difficulty: medium
// tags: array, sorting, top 150, meta, grind 75, citadel

// constraints
// 1 <= intervals.length <= 10^4
// intervals[i].length == 2
// 0 <= start_i <= end_i <= 10^4

// solution: sort + min/max
// complexity
// run-time: O(n*log n)
// space: O(1)!
std::vector<std::vector<int>> mergeIntervals(
        std::vector<std::vector<int>>& intervals)
{
    std::sort(intervals.begin(), intervals.end());

    int i = 1;
    while (i < intervals.size()) {
        if (intervals[i][0] <= intervals[i-1][1]) {
            intervals[i][0] = std::min(intervals[i][0], intervals[i-1][0]);
            intervals[i][1] = std::max(intervals[i][1], intervals[i-1][1]);
            // TODO: more efficient?
            intervals.erase(intervals.begin() + i-1);
        } else {
            ++i;
        }
    }

    return intervals;
}

// solution: sort + max
// complexity
// run-time: O(n*log n)
// space: O(n)
std::vector<std::vector<int>> mergeIntervals2(
        std::vector<std::vector<int>>& intervals)
{
    std::sort(intervals.begin(), intervals.end());
    std::vector<std::vector<int>> ans;

    for (const auto& start_end : intervals) {
        if (!ans.empty() && start_end[0] <= ans.back()[1]) {
            ans.back()[1] = std::max(ans.back()[1], start_end[1]);
        } else {
            ans.push_back(start_end);
        }
    }

    return ans;
}

// TODO: add unit tests
