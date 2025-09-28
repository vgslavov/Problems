#include <algorithm>
#include <vector>

// tags: sliding window

// solution: sliding window, longest
// complexity:
// run-time: O(n)
// space: O(1)
int subarraySumLongest(const std::vector<int>& nums, int target)
{
    int left = 0;
    int ans = 0;
    int winSum = 0;

    for (int right = 0; right != nums.size(); ++right) {
        winSum += nums[right];

        while (winSum > target) {
            winSum -= nums[left];
            ++left;
        }

        // window is valid here
        ans = std::max(ans, right-left+1);
    }

    return ans;
}