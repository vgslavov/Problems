#include <string>
#include <unordered_map>
#include <vector>

// leetcode: 438
// tags: sliding window

// solution: sliding window + map
// complexity:
// run-time: O(n)
// space: O(26) ~ O(1)
std::vector<int> findAllAnagrams(
    const std::string& original,
    const std::string& check)
{
    if (check.size() > original.size()) {
        return std::vector<int>{};
    }

    std::unordered_map<char, int> checkWin;

    for (const auto& c : check) {
        ++checkWin[c];
    }

    std::unordered_map<char, int> currWin;
    int left = 0;
    std::vector<int> ans;

    for (size_t right = 0; right != original.size(); ++right) {
        // add char to current window
        ++currWin[original[right]];

        // wait until current window extends to match check size
        if (right-left+1 < check.size()) {
            continue;
        }

        // we have a match!
        if (currWin == checkWin) {
            ans.push_back(left);
        }

        // shrink window from left
        if (currWin[original[left]] > 1) {
            --currWin[original[left]];
        } else {
            currWin.erase(original[left]);
        }

        ++left;
    }

    return ans;
}