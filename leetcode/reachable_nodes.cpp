#include <unordered_map>
#include <unordered_set>
#include <vector>

// number: 2368
// title: Reachable Nodes With Restrictions
// url: https://leetcode.com/problems/reachable-nodes-with-restrictions/
// section: graph
// difficulty: medium
// tags: array, hash table, dfs, bfs, union find, graph

// constraints:
// 2 <= n <= 10^5
// edges.length == n - 1
// edges[i].length == 2
// 0 <= a_i, b_i < n
// a_i != b_i
// edges represents a valid tree.
// 1 <= restricted.length < n
// 1 <= restricted[i] < n
// All the values of restricted are unique.

// solution: recursive DFS
// complexity:
// run-time: O(n + e)
// space: O(n + e)

std::unordered_map<int, std::vector<int>> graph;
std::unordered_set<int> seen;
std::unordered_set<int> restrictedSet;

void dfs(int node)
{
    for (const auto& neighbor: graph[node]) {
        auto it = seen.find(neighbor);
        if (it != seen.end()) {
            continue;
        }

        it = restrictedSet.find(neighbor);
        if (it != restrictedSet.end()) {
            continue;
        }

        seen.insert(neighbor);
        dfs(neighbor);
    }
}

int reachableNodes(int n, const std::vector<std::vector<int>>& edges, std::vector<int>& restricted)
{
    // build adjacency list
    for (const auto& e : edges) {
        graph[e[0]].push_back(e[1]);
        graph[e[1]].push_back(e[0]);
    }

    seen.insert(0);
    for (const auto& r : restricted) {
        restrictedSet.insert(r);
    }

    dfs(0);
    return seen.size();
}

// TODO: add tests cases & improve performance