#include <algorithm>
#include <vector>

// number: 1854
// title: Maximum Population Year
// url: https://leetcode.com/problems/maximum-population-year/
// difficulty: medium
// tags: array, counting, prefix sum

// constraints:
// 1 <= logs.length <= 100
// 1950 <= logs[i][0] < logs[i][1] <= 250

// solution: difference array + prefix sum
// time complexity: O(n)
// space complexity: O(n)
int maxPopulation(const std::vector<std::vector<int>>& logs)
{
    int firstYear = 1950;
    int lastYear = 2050;

    // build diff array
    std::vector<int> diff(lastYear-firstYear);

    for (const auto& start_end : logs) {
        ++diff[start_end[0]-firstYear];
        if ((start_end[1]-firstYear) < diff.size()) {
            --diff[start_end[1]-firstYear];
        }
    }

    // build prefix sum
    std::vector<int> prefix{diff[0]};

    for (size_t i = 1; i != diff.size(); ++i) {
        prefix.push_back(prefix.back()+diff[i]);
    }

    // find index of max population
    // index is the year minus firstYear
    return std::distance(prefix.begin(),
                         std::max_element(prefix.begin(), prefix.end()))
                        +firstYear;
}