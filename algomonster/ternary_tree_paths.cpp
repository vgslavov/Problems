#include <cstddef>
#include <string>
#include <vector>

// similar: 257
// tags: dfs, tree, backtracking

struct Node {
    int val;
    std::vector<Node*> children;
};

void dfs(
    Node* node,
    std::vector<std::string>& path,
    std::vector<std::string>& paths)
{
    if (!node) {
        return;
    // leaf node: append to results
    } else if (node->children.empty()) {
        path.push_back(std::to_string(node->val));

        // ala Python join
        std::string p;
        for (size_t i = 0; i < path.size(); ++i) {
            if (i > 0) p += "->";
            p += path[i];
        }

        paths.push_back(p);
        path.pop_back();
        return;
    }

    // DFS on each child
    for (Node* child : node->children) {
        path.push_back(std::to_string(node->val));
        dfs(child, path, paths);
        // backtrack
        path.pop_back();
    }
}

// solution: AlgoMonster* backtrack recursive dfs
// complexity:
// run-time: O(n)
// space: O(n)
std::vector<std::string> ternary_tree_paths(Node* root)
{
    std::vector<std::string> ans;
    std::vector<std::string> path;
    dfs(root, path, ans);
    return ans;
}