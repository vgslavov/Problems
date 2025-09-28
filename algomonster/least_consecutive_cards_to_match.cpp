#include <algorithm>
#include <limits>
#include <vector>
#include <unordered_map>

// tags: sliding window

// complexity:
// run-time: O(n)
// space: O(n)
int leastConsecutiveCardsToMatch(const std::vector<int>& cards)
{
    int left = 0;
    std::unordered_map<char, int> currWin;
    int ans = std::numeric_limits<int>::max();

    for (int right = 0; right != cards.size(); ++right) {
        ++currWin[cards[right]];

        while (currWin[cards[right]] > 1) {
            ans = std::min(ans, right-left+1);
            --currWin[cards[left]];

            if (currWin[cards[left]] == 0) {
                currWin.erase(cards[left]);
            }
            ++left;
        }
    }

    return ans != std::numeric_limits<int>::max() ? ans : -1;
}