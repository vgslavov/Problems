#include <map>
#include <string>
#include <utility>

// number: 208
// title: Implement Trie (Prefix Tree)
// url: https://leetcode.com/problems/implement-trie-prefix-tree/
// section: trie (prefix tree)
// difficulty: medium
// tags: hash table, string, design, trie, top 150, citadel

// constraints
// 1 <= word.length, prefix.length <= 2000
// word and prefix consist only of lowercase English letters.
// At most 3 * 10^4 calls in total will be made to insert, search, and
// startsWith.

// complexity
// run-time: O(n)
// space: O(n*m)
class Trie {
public:
    using ChildrenMap = std::map<char, Trie*>;

    Trie() = default;

    void insert(const std::string& word) {
        Trie* curr = this;

        for (const auto& c: word) {
            ChildrenMap& children = curr->d_children;
            auto itr = children.find(c);
            if (itr == children.end()) {
                children[c] = new Trie();
                // if we had to move it
                //Trie newTrie = Trie();
                //children.insert(std::make_pair(c, std::move(newTrie)));
            }

            curr = curr->d_children[c];
        }

        curr->isendword(true);
    }

    bool search(const std::string& word) {
        return searchHelper(word, true);
    }

    bool startsWith(const std::string& prefix) {
        return searchHelper(prefix);
    }

    void isendword(bool val) { d_isendword = val; }

    bool isendword() const { return d_isendword; }

private:
    bool searchHelper(const std::string& word, bool checkEndWord=false) {
        Trie* curr = this;

        for (const auto& c: word) {
            // can access private members of other instances of same class!
            ChildrenMap& children = curr->d_children;
            const auto itr = children.find(c);
            if (itr == children.end()) {
                return false;
            }

            curr = curr->d_children[c];
        }

        if (!checkEndWord || curr->isendword()) {
            return true;
        } else {
            return false;
        }
    }

    ChildrenMap d_children;
    bool        d_isendword = false;
};

// Your Trie object will be instantiated and called as such:
Trie* obj = new Trie();
obj->insert(word);
bool param_2 = obj->search(word);
bool param_3 = obj->startsWith(prefix);
