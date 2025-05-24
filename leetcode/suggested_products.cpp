#include <string>
#include <vector>
#include <utility>

// number: 1268
// title: Search Suggestions System
// url: https://leetcode.com/problems/search-suggestions-system/
// section: citadel
// difficulty: medium
// tags: array, string, binary search, trie, sorting, heap, prio queue, citadel

// constraints
// n: len(products)
// m: len(searchWord)
// 1 <= n <= 1000
// 1 <= len(products[i]) <= 3000
// 1 <= sum(len(products[i])) <= 2 * 10^4
// All the strings of products are unique.
// products[i] consists of lowercase English letters.
// 1 <= m <= 1000
// searchWord consists of lowercase English letters.
//
// If there are more than three products with a common prefix
// return the three lexicographically minimums products.

bool check(const std::string& item, const std::string& prefix)
{
    return item.substr(0, prefix.size()) >= prefix;
}

// duplicates, return left-most
// run-time: O(log n)
// space: O(1)
int binarySearch(
    const std::vector<std::string>& products, const std::string& prefix)
{
    int left = 0;
    int right = products.size();

    while (left < right) {
        int mid = left + (right-left)/2;

        if (check(products[mid], prefix)) {
            right = mid;
        } else {
            left = mid+1;
        }
    }

    return left;
}

// solution: binary search
// complexity
// run-time: O(n*log n + m*log n)
// space: O(1)
std::vector<std::vector<std::string>> suggestedProducts(
    std::vector<std::string>& products, const std::string& searchWord)
{
    std::vector<std::vector<std::string>> ans;
    std::string prefix;
    size_t k = 3;

    // O(n*log n)
    std::sort(products.begin(), products.end());

    // O(m*log n)
    for (const auto& c: searchWord) {
        prefix += c;

        int left = binarySearch(products, prefix);
 
        std::vector<std::string> subAns;

        size_t end = std::min(products.size(), left+k);
        for (size_t i = left; i != end; ++i) {
            if (prefix != products[i].substr(0, prefix.size())) {
                break;
            }
            subAns.push_back(products[i]);
        }

        ans.push_back(subAns);
    }

    return ans;
}

// TODO: add unit tests & solve using trie
