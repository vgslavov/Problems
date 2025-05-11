#include <vector>
#include <unordered_map>

// number: 1971
// title: Valid Path in a Graph
// url: https://leetcode.com/problems/valid-path-in-a-graph/
// section: graph
// difficulty: easy
// tags: dfs, bfs, union find, graph

// constraints:
// 1 <= n <= 2 * 10^5
// 0 <= edges.length <= 2 * 10^5
// edges[i].length == 2
// 0 <= u_i, v_i <= n - 1
// u_i != v_i
// 0 <= source, destination <= n - 1
// There are no duplicate edges.
// There are no self edges.

// solution: recursive DFS
// complexity:
// run-time: O(n + e)
// space: O(n + e)

std::unordered_map<int, std::vector<int>> graph;
std::vector<bool> seen;

bool dfs(int node, int destination)
{
    // base case
    if (node == destination) {
        return true;
    }

    for (const auto& neighbor : graph[node]) {
        if (seen[neighbor]) {
            continue;
        }

        seen[neighbor] = true;

        if (dfs(neighbor, destination)) {
            return true;
        }
    }

    return false;
}

bool validPath(int n, const std::vector<std::vector<int>>& edges, int source, int destination)
{
    // init
    seen = std::vector<bool>(n, false);

    if (source == destination) {
        return true;
    }

    // build adjacency list
    for (const auto& e : edges) {
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }

    seen[source] = true;
    return dfs(source, destination);
}

// TODO: add unit tests