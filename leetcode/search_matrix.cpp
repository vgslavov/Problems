#include <algorithm>
#include <vector>

// number: 74
// title: Search a 2D Matrix
// url: https://leetcode.com/problems/search-a-2d-matrix/
// section: binary search
// difficulty: medium
// tags: array, binary search, matrix

// constraints
// m == matrix.length
// n == matrix[i].length
// 1 <= m, n <= 100
// -10^4 <= matrix[i][j], target <= 10^4
// Each row is sorted in non-decreasing order.
// The first integer of each row is greater than the last integer of the previous row.

// complexity
// run-time: O(log m)
// space: O(1)
int findRow(const std::vector<std::vector<int>>& matrix, int target)
{
    if (matrix.empty()) {
        return -1;
    }

    int left = 0;
    int right = matrix.size()-1;
    int rows = matrix.size();
    int cols = matrix[0].size();

    // outside this row's range
    if (target < matrix[0][0] ||
        target > matrix[rows-1][cols-1])
    {
        return -1;
    }

    while (left <= right) {
        int mid = left + (right-left)/2;

        if (matrix[mid][0] <= target &&
            target <= matrix[mid][cols-1])
        {
            return mid;
        } else if (matrix[mid][0] > target) {
            right = mid-1;
        } else {
            left = mid+1;
        }
    }

    return -1;
}

// solution: manual binary search + lower_bound
// complexity
// run-time: O(log m + log n)
// space: O(1)
bool searchMatrix(const std::vector<std::vector<int>>& matrix, int target)
{
    int row = findRow(matrix, target);
    if (row == -1) {
        return false;
    }

    auto col = std::lower_bound(matrix[row].begin(), matrix[row].end(), target);
    if (col == matrix[row].end() || *col != target) {
        return false;
    }

    return true;
}
