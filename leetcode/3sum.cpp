#include <algorithm>
#include <copy>
#include <iterator>
#include <map>
#include <set>
#include <vector>

// number: 15
// section: two pointers
// difficulty: medium
// tags: array, two pointers, sorting, top 150, meta

// constraints
// 3 <= nums.length <= 3000
// -10^5 <= nums[i] <= 10^5

// solution: brute-force, map + set
// run-time: O(n^3), too slow, TLE
// space: O(n)
std::vector<std::vector<int>> threeSum(const std::vector<int>& nums)
{
    std::map<int, std::vector<int>> counts;

    for (int i = 0; i != nums.size(); ++i) {
        auto it = counts.find(nums[i]);

        // TODO: user insert_or_assign?
        if (it != counts.end()) {
            counts[nums[i]].push_back(i);
        } else {
            counts[nums[i]] = std::vector<int>{i};
        }
    }

    std::set<std::vector<int>> seen;

    for (int i = 0; i != nums.size(); ++i) {
        for (int j = i+1; j != nums.size(); ++j) {
            // not possible
            //if (i == j) {
            //    continue;
            //}

            int third = -nums[i]-nums[j];

            auto it = counts.find(third);
            if (it == counts.end()) {
                continue;
            }

            // need values from counts[third], not indices!
            for (const auto& k: counts[third]) {
                if (i != k && j != k) {
                    std::vector<int> v{nums[i],nums[j],third};
                    std::sort(v.begin(), v.end());
                    seen.insert(v);
                    break;
                }
            }
        }
    }

    std::vector<std::vector<int>> ans;
    std::copy(seen.begin(), seen.end(), std::back_inserter(ans));
    std::sort(ans.begin(), ans.end());

    return ans;
}
