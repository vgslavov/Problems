#include <queue>
#include <set>
#include <vector>

// tags: bfs, graph

// solution: iterative bfs
// complexity:
// run-time: O(n+m)
// space: O(n)
int shortestPath(std::vector<std::vector<int>> graph, int a, int b)
{
    int ans = 0;

    // start at a
    std::queue<int> queue;
    queue.push(a);
    std::set<int> seen;
    seen.insert(a);

    while (!queue.empty()) {
        size_t size = queue.size();

        while (size) {
            int node = queue.front();
            queue.pop();

            // reach b
            if (node == b) {
                return ans;
            }

            for (const auto& neighbor : graph[node]) {
                if (seen.find(neighbor) != seen.end()) {
                    continue;
                }

                seen.insert(neighbor);
                queue.push(neighbor);
            }

            --size;
        }

        ++ans;
    }

    return ans;
}