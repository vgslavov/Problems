#include <queue>
#include <vector>

// tags: heap

// solution: max heap
// complexity:
// run-time: O(n*log k)
// space: O(k)
std::vector<std::vector<int>> findKClosestPoints(
    const std::vector<std::vector<int>> points,
    int k)
{
    using pi = std::pair<int, std::pair<int, int>>;
    // max heap
    // values: distance, (x,y) coordinates
    std::priority_queue<pi, std::vector<pi>> heap;

    for (const auto& x_y: points) {
        int distance = x_y[0]*x_y[0] + x_y[1]*x_y[1];

        heap.push(std::make_pair(distance, std::make_pair(x_y[0], x_y[1])));

        if (heap.size() > k) {
            heap.pop();
        }
    }

    std::vector<std::vector<int>> ans;
    while (!heap.empty()) {
        auto point = heap.top().second;
        ans.push_back({point.first, point.second});
        heap.pop();
    }

    std::sort(ans.begin(), ans.end());
    return ans;
}