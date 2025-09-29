#include <queue>
#include <vector>

// tags: heap

// solution: max heap
// complexity:
// run-time: O(n^2*log k)
// space: O(k)
int findKSmallest(const std::vector<std::vector<int>> matrix, int k)
{
    // max heap
    std::priority_queue<int> heap;

    for (size_t i = 0; i != matrix.size(); ++i) {
        for (size_t j = 0; j != matrix[i].size(); ++j) {
            heap.push(matrix[i][j]);

            if (heap.size() > k) {
                heap.pop();
            }
        }
    }

    return heap.top();
}

// TODO: solve using min heap in O(n+k*log n)