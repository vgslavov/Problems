#include <algorithm>
#include <string>
#include <vector>

// number: 670
// title: Maximum Swap
// url: https://leetcode.com/problems/maximum-swap/
// section: meta
// difficulty: medium
// tags: math, greedy, meta

// constraints
// 1 <= num <= 10^8

// non-solution: brute force
// complexity
// run-time: O(n^), TLE
// space: O(n)
int maxSwap(int num)
{
    std::string numStr = std::to_string(num);
    int ans = num;

    for (size_t i = 0; i != numStr.size(); ++i) {
        for (size_t j = i+1; j != numStr.size(); ++j) {
            std::string numSwap = numStr;

            std::swap(numSwap[i], numSwap[j]);
            ans = std::max(ans, std::stoi(numSwap));
        }
    }

    return ans;
}

// solution: LeetCode greedy
// complexity
// run-time: O(n)
// space: O(n)
int maxSwap2(int num)
{
    std::string numStr(std::to_string(num));
    std::vector<int> maxIdx(numStr.size());
    maxIdx.back() = numStr.size()-1;

    // reverse pass: find max b/w i & end
    // skip last
    for (size_t i = numStr.size()-1; i != 0;) {
        --i;
        maxIdx[i] = numStr[i] > numStr[maxIdx[i+1]] ? i : maxIdx[i+1];
    }

    // forward pass: swap
    for (size_t i = 0; i != numStr.size(); ++i) {
        if (numStr[i] >= numStr[maxIdx[i]]) {
            continue;
        }

        // swap only if current < max to the right
        std::swap(numStr[i],numStr[maxIdx[i]]);
        return std::stoi(numStr);
    }

    // no swaps
    return num;
}

// TODO: add unit tests