#include <limits>
#include <vector>

// number: 718
// section: citadel
// difficulty: medium
// tags: array, binary search, dp, sliding window, rolling hash, hash function

// constraints
// n: len(nums1)
// m: len(nums2)
// 1 <= n, m <= 1000
// 0 <= nums1[i], nums2[i] <= 100


// solution: Leetcode bottom-up iterative 2DP like LCS
// complexity
// run-time: O(n*m)
// space: O(n*m)
int findLength(std::vector<int>& nums1, std::vector<int>& nums2) {
    // init
    std::vector<std::vector<int>> dp(
        nums1.size()+1, std::vector<int>(nums2.size()+1));

    for (int i = nums1.size()-1; i >= 0; --i) {
        for (int j = nums2.size()-1; j >= 0; --j) {
            if (nums1[i] == nums2[j]) {
                // recurrence relation
                dp[i][j] = dp[i+1][j+1] + 1;
            }
        }
    }

    int ans = std::numeric_limits<int>::min();

    for (int i = 0; i != nums1.size(); ++i) {
        for (int j = 0; j != nums2.size(); ++j) {
            ans = std::max(ans, dp[i][j]);
        }
    }

    // TODO: use STL
    //return *std::max_element(dp.begin(), dp.end());

    return ans;
}

// TODO: add unit tests
