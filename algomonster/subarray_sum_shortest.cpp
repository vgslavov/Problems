#include <algorithm>
#include <vector>

// tags: sliding window

// solution: sliding window, shortest
// complexity:
// run-time: O(n)
// space: O(1)
int subarraySumShortest(const std::vector<int>& nums, int target)
{
    int left = 0;
    int winSum = 0;
    int ans = nums.size();

    for (int right = 0; right != nums.size(); ++right) {
        winSum += nums[right];

        while (winSum >= target) {
            ans = std::min(ans, right-left+1);
            winSum -= nums[left];
            ++left;
        }
    }

    return ans;
}