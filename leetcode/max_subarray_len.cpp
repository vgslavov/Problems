#include <map>
#include <utility>
#include <vector>

// number: 2958
// section: citadel
// difficulty: medium
// tags: array, hash table, sliding window, citadel

// constraints
// 1 <= nums.length <= 10^5
// 1 <= nums[i] <= 10^9
// 1 <= k <= nums.length
// An array is called good if the frequency of each element in this array is
// less than or equal to k.
// Return the length of the longest good subarray of nums.

// solution: sliding window + map
// complexity
// run-time: O(n)
// space: O(n)
int maxSubarrayLength(std::vector<int>& nums, int k)
{
    int left = 0;
    int ans = 0;
    std::map<int, int> freqs;

    for (int right = 0; right != nums.size(); ++right) {
        // expand window while freqs < k
        auto iter = freqs.find(nums[right]);
        if (iter != freqs.end()) {
            freqs[nums[right]] += 1;
        } else {
            freqs[nums[right]] = 1;
        }

        // shrink window
        while (freqs[nums[right]] > k) {
            freqs[nums[left]] -= 1;
            left += 1;
        }

        // add 1!
        ans = std::max(ans, right-left+1);
    }

    return ans;
}

// TODO: add unit tests
