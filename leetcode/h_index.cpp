#include<algorithm>
#include<vector>

// number: 274
// section: array / string
// difficulty: medium
// tags: array, sorting, counting sort, top 150

// constraints:
// n == citations.length
// 1 <= n <= 5000
// 0 <= citations[i] <= 1000

// solution: LeetCode sorting
// complexity:
// time: O(n*log n)
// space: O(1)
int hIndex(std::vector<int>& citations)
{
    // descending order
    std::sort(citations.begin(), citations.end(), std::greater<int>());

    int i = 0;
    // keep going until we find the first citation that is less than the index
    while (i < citations.size() && citations[i] > i) {
        ++i;
    }

    return i;
}

// TODO: implement counting sort solution
// TODO: add unit tests