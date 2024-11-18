#include <algorithm>
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
//
// return all the triplets [nums[i], nums[j], nums[k]]
// such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
// the solution set must not contain duplicate triplets

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

// complexity
// run-time O(n)
// space: O(n)
void twoSum(const std::vector<int>& nums, int k, std::set<std::vector<int>>& ans)
{
    if (nums.empty()) {
        return;
    }

    std::set<int> seen;

    for (int i = k+1; i != nums.size(); ++i) {
        int diff = -nums[i]-nums[k];

        auto it = seen.find(diff);
        if (it != seen.end()) {
            std::vector<int> v{nums[i],nums[k],diff};
            std::sort(v.begin(), v.end());
            ans.insert(v);

            // eliminate same indices
            if (i == k || i == diff || k == diff) {
                continue;
            }

            // optimization: skip dupes
            if (i != 0 && nums[i-1] == nums[k]) {
                continue;
            }
        }

        seen.insert(nums[i]);
    }
}

// solution: LeetCode, sort + two-sum using set
// run-time: O(n*log n + n^2) ~ O(n^2)
// space: O(n)
std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
    std::vector<std::vector<int>> ans;

    if (nums.empty()) {
        return ans;
    }

    std::sort(nums.begin(), nums.end());
    std::set<std::vector<int>> seen;

    for (int k = 0; k != nums.size(); ++k) {
        // optimization: 3rd num must be negative,
        // otherwise can't add up to 0
        if (nums[k] > 0) {
            break;
        }

        // optimization: skip dupes (sorted)
        if (k != 0 && nums[k] == nums[k-1]) {
            continue;
        }

        twoSum(nums, k, seen);
    }

    std::copy(seen.begin(), seen.end(), std::back_inserter(ans));
    std::sort(ans.begin(), ans.end());

    return ans;
}

// TODO: add unit tests
