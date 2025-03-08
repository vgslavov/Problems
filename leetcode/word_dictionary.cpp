#include <string>
#include <unordered_map>

// number: 211
// section: trie
// difficulty: medium
// tags: string, dfs, design, trie, top 150

// contraints
// m: len(word)
// n: words
// 1 <= m <= 25
// word in addWord consists of lowercase English letters.
// word in search consist of '.' or lowercase English letters.
// There will be at most 2 dots in word for search queries.
// At most 10^4 calls will be made to addWord and search.

// solution: Nursultan's LeetCode recursive dfs + trie
// complexity
// run-time: O(m)
// space: O(n*m)?
struct TrieNode {
    using ChildrenMap = std::unordered_map<char, TrieNode*>;

    TrieNode() = default;

    ChildrenMap children;
    bool isWord = false;
};

class WordDictionary {
public:
    WordDictionary() = default;

    // TODO: recursively free allocated mem
    //~WordDictionary() {
    //    while (d_root != nullptr) {
    //        delete d_root;
    //    }
    //}

    void addWord(const std::string& word) {
        TrieNode* node = d_root;

        for (const auto& ch: word) {
            TrieNode::ChildrenMap& children = node->children;
            auto it = children.find(ch);
            if (it == children.end()) {
                node->children[ch] = new TrieNode();
            }
            node = node->children[ch];
        }

        node->isWord = true;
    }

    bool search(const std::string& word) {
        return dfs(0, d_root, word);
    }
private:
    bool dfs(int i, TrieNode* node, const std::string& word) {
        if (i == word.size()) {
            return node->isWord;
        }

        char ch = word[i];

        // compare to char constant (single quotes)!
        // not string literal (double quotes)
        if (ch == '.') {
            for (const auto& child : node->children) {
                if (dfs(i+1, node->children[child.first], word)) {
                    return true;
                }
            }
        } else {
            auto it = node->children.find(ch);
            if (it != node->children.end()) {
                if (dfs(i+1, node->children[ch], word)) {
                    return true;
                }
            }
        }

        return false;
    }

    TrieNode* d_root = new TrieNode();
};

// Your WordDictionary object will be instantiated and called as such:
WordDictionary* obj = new WordDictionary();
obj->addWord(word);
bool param_2 = obj->search(word);
