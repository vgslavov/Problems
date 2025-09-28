#include <queue>
#include <vector>

// tags: heap, sliding window, monotonic queue

// solution: max heap + sliding window
// complexity:
// run-time: O(n*log k)
// space: O(k)
std::vector<int> slidingWindowMax(const std::vector<int>& nums, int k)
{
    std::vector<int> ans;
    int left = 0;

    // max heap: value, index
    using pi = std::pair<int, int>;
    std::priority_queue<pi, std::vector<pi>> heap;

    for (int right = 0; right != nums.size(); ++right) {
        heap.push(std::make_pair(nums[right], right));

        // reached window size
        if (right >= k-1) {
            // pop all indices outside window: O(log k)
            while (heap.top().second < left) {
                heap.pop();
            }

            // window max
            ans.push_back(heap.top().first);

            // slide window
            ++left;
        }
    }

    return ans;
}

// TODO: solve in O(n) using deque