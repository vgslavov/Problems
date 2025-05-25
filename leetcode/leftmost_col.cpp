#include <algorithm>
#include <limits>
#include <vector>

// number: 1428
// title: Leftmost Column with at Least a One
// url: https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
// section: assessments
// difficulty: medium
// tags: array, binary search, matrix, interactive, meta

// constraints
// rows == mat.length
// cols == mat[i].length
// 1 <= rows, cols <= 100
// mat[i][j] is either 0 or 1.
// mat[i] is sorted in non-decreasing order.

// Submissions making more than 1000 calls to BinaryMatrix.get will be judged
// Wrong Answer.

// This is the BinaryMatrix's API interface.
// You should not implement it, or speculate about its implementation
class BinaryMatrix {
  public:
    int get(int row, int col);
    std::vector<int> dimensions();
};

int binarySearch(BinaryMatrix &binaryMatrix, int row, int len, int k)
{
    int left = 0;
    int right = len;

    while (left < right) {
        int mid = left + (right-left) / 2;

        int cell = binaryMatrix.get(row, mid);

        if (cell >= k) {
            right = mid;
        } else {
            left = mid+1;
        }
    }

    return left;
}
int leftmostCol(BinaryMatrix &binaryMatrix)
{
    auto dim = binaryMatrix.dimensions();
    int rows = dim[0];
    int cols = dim[1];
    int ans = std::numeric_limits<int>::max();

    for (int i = 0; i != rows; ++i) {
        // fix the row &
        // search for the leftmost column with a one
        int j = binarySearch(binaryMatrix, i, cols, 1);
        if (j < cols && binaryMatrix.get(i, j) == 1) {
            ans = std::min(ans, j);
        }
    }

    return ans != std::numeric_limits<int>::max() ? ans : -1;
}
