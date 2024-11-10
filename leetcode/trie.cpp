#include <map>
#include <utility>

// number: 208
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
#include <map>

class Trie {
public:
    using ChildrenMap = std::map<char, Trie>;

    Trie()
    : d_isendword(false)
    {
    }

    void insert(const string& word) {
        Trie* curr = this;

        for (const auto& c: word) {
            ChildrenMap& children = curr->children();
            auto itr = children.find(c);
            if (itr == children.end()) {
                children[c] = Trie();
                // if we had to move it
                //Trie newTrie = Trie();
                //children.insert(std::make_pair(c, std::move(newTrie)));
            }

            curr = &curr->children()[c];
        }

        curr->isendword(true);
    }

    bool search(const string& word) {
        return searchHelper(word, true);
    }

    bool startsWith(const string& prefix) {
        return searchHelper(prefix);
    }

    void isendword(bool val) { d_isendword = val; }

    ChildrenMap& children() { return d_children; }

    bool isendword() const { return d_isendword; }

private:
    bool searchHelper(const string& word, bool checkEndWord=false) {
        Trie* curr = this;

        for (const auto& c: word) {
            ChildrenMap& children = curr->children();
            const auto itr = children.find(c);
            if (itr == children.end()) {
                return false;
            }

            curr = &curr->children()[c];
        }

        if (!checkEndWord || curr->isendword()) {
            return true;
        } else {
            return false;
        }
    }

    ChildrenMap d_children;
    bool        d_isendword;
};

// Your Trie object will be instantiated and called as such:
Trie* obj = new Trie();
obj->insert(word);
bool param_2 = obj->search(word);
bool param_3 = obj->startsWith(prefix);
