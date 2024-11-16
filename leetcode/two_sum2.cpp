#include <algorithm>
#include <iterator>
#include <vector>

// number: 167
// section: two pointers
// difficulty: medium
// tags: array, two pointers, binary search, top 150

// constraints
// 2 <= numbers.length <= 3 * 10^4
// -1000 <= numbers[i] <= 1000
// numbers is sorted in non-decreasing order.
// -1000 <= target <= 1000
// The tests are generated such that there is exactly one solution.

// solution: C++ lower_bound
// complexity
// run-time: O(n*log n)
// space: O(1)
std::vector<int> twoSum2(const std::vector<int>& numbers, int target)
{
    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        int diff = target - *it;

        auto dit = std::lower_bound(numbers.begin(), numbers.end(), diff);

        // not found or pointing to same element
        if (dit == numbers.end() or it == dit) {
            continue;
        }

        if ((*it+*dit) == target) {
            int first = std::distance(numbers.begin(), it);
            int second = std::distance(numbers.begin(), dit);

            // 1-indexed!
            std::vector<int> ans{first+1,second+1};
            std::sort(ans.begin(), ans.end());

            return ans;
        }
    }

    return std::vector<int>{-1,-1};
}

// complexity
// run-time: O(log n)
// space: O(1)
int binarySearch(const std::vector<int>& numbers, int k) {
    int left = 0;
    int right = numbers.size()-1;

    while (left <= right) {
        int mid = left + (right-left)/2;

        if (numbers[mid] == k) {
            return mid;
        } else if (numbers[mid] < k) {
            left = mid+1;
        } else {
            right = mid-1;
        }
    }

    return left;
}

// solution: manual binary search
// complexity
// run-time: O(n*log n)
// space: O(1)
std::vector<int> twoSum2_2(const std::vector<int>& numbers, int target)
{
    for (int i = 0; i != numbers.size(); ++i) {
        int diff = target - numbers[i];

        int j = binarySearch(numbers, diff);

        // not found or pointing to same element
        if (j < 0 || j > numbers.size()-1 || numbers[j] != diff || i == j) {
            continue;
        }

        if ((numbers[i] + numbers[j]) == target) {
            // 1-indexed!
            std::vector<int> ans{i+1,j+1};
            std::sort(ans.begin(), ans.end());

            return ans;
        }
    }

    return std::vector<int>{-1,-1};
}

// TODO: add unit tests
