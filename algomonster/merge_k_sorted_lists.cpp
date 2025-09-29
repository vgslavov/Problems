#include <queue>
#include <vector>

// tags: heap

// solution: min heap
// complexity:
// run-time: O(n*log n)
// space: O(n)
std::vector<int> mergeKSortedLists2(const std::vector<std::vector<int>> lists)
{
    // min heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> heap;
    std::vector<int> ans;

    for (const auto& l : lists) {
        for (const auto& n : l) {
            heap.push(n);
        }
    }

    while (!heap.empty()) {
        ans.push_back(heap.top());
        heap.pop();
    }

    return ans;
}

// solution: AlgoMonster min heap, uses sorting requirement
// complexity:
// run-time: O(n*log k)
// space: O(k)
std::vector<int> mergeKSortedLists(const std::vector<std::vector<int>> lists)
{
    // min heap
    // values: 1st value, list index, element index
    // maintains only k elements in heap at any time
    using T = std::tuple<int, int, int>;
    std::priority_queue<T, std::vector<T>, std::greater<T>> heap;
    std::vector<int> ans;

    for (size_t i = 0; i != lists.size(); ++i) {
        if (lists[i].empty()) {
            continue;
        }

        // push first element of each list
        heap.push(std::make_tuple(lists[i][0], i, 0));

    }

    while (!heap.empty()) {
        auto [val, listNum, index] = heap.top();
        heap.pop();

        ans.push_back(val);

        // if more in this list, push next
        if (index + 1 < lists[listNum].size()) {
            heap.push(std::make_tuple(lists[listNum][index + 1], listNum, index + 1));
        }
    }

    return ans;
}