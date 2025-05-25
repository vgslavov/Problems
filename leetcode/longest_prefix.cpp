#include <iostream>
#include <map>

// number: 14
// title: Longest Common Prefix
// url: https://leetcode.com/problems/longest-common-prefix/
// section: array/string
// difficulty: easy
// tags: string, trie, top 150

// constraints
// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters.

// complexity
// run-time: O(n)
// space: O(1)
class Trie {
public:
    // need map, we'll be iterating over keys
    using ChildrenMap = std::map<char, Trie>;

    Trie()
    : d_count(0) {}

    void insert(const std::string& word) {
        Trie* node = this;
        node->count() += 1;

        for (const auto& c: word) {
            ChildrenMap& children = node->d_children;
            auto iter = children.find(c);
            if (iter == children.end()) {
                children[c] = Trie();
            }

            node = &node->d_children[c];
            node->count() += 1;
        }
    }

    std::string commonPrefix() {
        Trie* node = this;
        std::string prefix;
        auto iter = node->d_children.begin();

        while (1) {
            if (node->d_children.empty()) {
                break;
            }

            // TODO: figure out iterator
            auto c = iter->first;
            ++iter;
            //if (iter == node->children().end()) {
            //    std::cout << "no children" << std::endl;
            //    break;
            //}

            if (node->count() != d_count) {
                if (!prefix.empty()) {
                    std::cout << "prefix:" << prefix << std::endl;
                    return prefix.substr(0, prefix.size()-1);
                } else {
                    std::cout << "empty prefix" << std::endl;
                    return "";
                }
            }

            prefix += c;
            node = &node->d_children[c];
        }

        if (node->count() != d_count) {
            std::cout << "prefix:" << prefix << std::endl;
            return prefix.substr(0, prefix.size()-1);
        }

        std::cout << "prefix:" << prefix << std::endl;

        return prefix;
    }

    int& count() { return d_count; }
    void count(int value) { d_count = value; }

private:
    ChildrenMap d_children;
    int         d_count;
};

// WIP solution: trie
// complexity:
// run-time: O(n)
// space: O(n)
std::string longestCommonPrefix(const std::vector<std::string>& strs) {
    Trie trie;

    for (const auto& w: strs) {
        trie.insert(w);
    }

    return trie.commonPrefix();
}
