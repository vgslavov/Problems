#include <vector>

// number: 1762
// title: Buildings With an Ocean View
// url: https://leetcode.com/problems/buildings-with-an-ocean-view/
// difficulty: medium
// tags: array, stack, monotonic stack

// constraints:
// 1 <= heights.length <= 10^5
// 1 <= heights[i] <= 10^9

// solution: vector as stack
// complexity:
// run-time: O(n)
// space: O(n)
std::vector<int> findBuildings(const std::vector<int>& heights)
{
    std::vector<int> ans;

    for (size_t i = 0; i != heights.size(); ++i) {
        while (!ans.empty() && heights[ans.back()] <= heights[i]) {
            ans.pop_back();
        }

        ans.push_back(i);
    }

    return ans;
}