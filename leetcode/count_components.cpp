#include <vector>
#include <unordered_map>

// number: 323
// title: Number of Connected Components in an Undirected Graph
// url: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
// section: graph
// difficulty: medium
// tags: dfs, bfs, union find, graph

// constraints:
// 1 <= n <= 2 * 10^4
// 0 <= edges.length <= 2 * 10^4
// edges[i].length == 2
// 0 <= u_i, v_i <= n - 1
// u_i != v_i
// There are no duplicate edges.

// solution: recursive DFS
// complexity:
// run-time: O(n + e)
// space: O(n + e)

std::unordered_map<int, std::vector<int>> graph;
std::vector<bool> seen;

void dfs(int node) {
    for (const auto& neighbor : graph[node]) {
        if (!seen[neighbor]) {
            seen[neighbor] = true;
            dfs(neighbor);
        }
    }
}

int countComponents(int n, std::vector<std::vector<int>>& edges)
{
    seen = std::vector<bool>(n, false);

    // build adjacency list
    for (const auto& e : edges) {
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }

    int ans = 0;
    for (size_t i = 0; i != n; ++i) {
        if (!seen[i]) {
            ++ans;
            seen[i] = true;
            dfs(i);
        }
    }

    return ans;
}

// TODO: add test cases