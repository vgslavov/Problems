#include <algorithm>
#include <vector>

// number: 57
// section: intervals
// difficulty: medium
// tags: array, interval

// constraints
// 0 <= intervals.length <= 10^4
// intervals[i].length == 2
// 0 <= start_i <= end_i <= 10^5
// intervals is sorted by start_i in ascending order.
// new_interval.length == 2
// 0 <= start <= end <= 10^5

bool merge(int start,
           int end,
           std::vector<std::vector<int>>& ans,
           bool append=true)
{
    if (!ans.empty() && start <= ans[ans.size()-1][1]) {
        ans[ans.size()-1][1] = std::max(ans[ans.size()-1][1], end);
        return true;
    } else if (append) {
        // use {}
        ans.push_back(std::vector<int>{start, end});
        return true;
    }
    return false;
}

// solution: intervals
// complexity
// run-time: O(n)
// space: O(n)
// TODO: refactor
std::vector<std::vector<int>> insertIntervals(
        std::vector<std::vector<int>>& intervals,
        std::vector<int>& newInterval)
{
    std::vector<std::vector<int>> ans;
    bool inserted = false;
    bool append = false;

    if (intervals.empty()) {
        return std::vector<std::vector<int>>(1, newInterval);
    }

    for (const auto& i : intervals) {
        if (!inserted) {
            if (newInterval[0] < i[0]) {
                append = true;
            } else {
                append = false;
            }

            inserted = merge(newInterval[0], newInterval[1], ans, append);
        }

        merge(i[0], i[1], ans);
    }

    if (!inserted) {
        merge(newInterval[0], newInterval[1], ans);
    }

    return ans;
}

// TODO: add unit tests
