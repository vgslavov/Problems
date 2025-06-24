#include <string>
#include <vector>

// number: 257
// title: Binary Tree Paths
// url: https://leetcode.com/problems/binary-tree-paths/
// section: binary tree general
// difficulty: easy
// tags: tree, dfs, backtracking, string, meta

// constraints
// The number of nodes in the tree is in the range [1, 100].
// -100 <= Node.val <= 100

 // Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
  
std::vector<std::string> paths;

std::string joinStr(const std::string& s1, const std::string& s2)
{
    return s1.empty() ? s2 : s1 + "->" + s2;
}

// pass by value to avoid modifying string after returns
void dfs(TreeNode* node, std::string path) {
    if (!node) {
        return;
    } else if (!node->left && !node->right) {
        paths.push_back(joinStr(path, std::to_string(node->val)));
        return;
    }

    path = joinStr(path, std::to_string(node->val));
    dfs(node->left, path);
    dfs(node->right, path);
}

// solution: recursive dfs
// complexity
// run-time: O(n)
// space: O(n)
std::vector<std::string> binaryTreePaths(TreeNode* root) {
    dfs(root, "");

    return paths;
}