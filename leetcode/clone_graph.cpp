#include <vector>
#include <unordered_map>

// number: 133
// title: Clone Graph
// url: https://leetcode.com/problems/clone-graph/
// section: graph
// difficulty: medium
// tags: graph, dfs, bfs, hash table, meta

// constraints
// The number of nodes in the graph is in the range [0, 100].
// 1 <= Node.val <= 100
// Node.val is unique for each node.
// There are no repeated edges and no self-loops in the graph.
// The Graph is connected and all nodes can be visited starting from the given node.

// Definition for a Node.
class Node {
public:
    int val;
    std::vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = std::vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = std::vector<Node*>();
    }
    Node(int _val, std::vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

// solution: recursive dfs
// complexity
// run-time: O(V + E)
// space: O(V)

std::unordered_map<Node*, Node*> visited;

Node* cloneGraph(Node* node)
{
    // base case
    if (node == nullptr) {
        return node;
    }

    auto it = visited.find(node);
    if (it != visited.end()) {
        return visited[node];
    }

    Node* cloneNode = new Node(node->val, {});
    visited[node] = cloneNode;

    for (auto & n : node->neighbors) {
        cloneNode->neighbors.push_back(cloneGraph(n));
    }

    return cloneNode;
}

// TODO: solve using iterative bfs & add unit tests