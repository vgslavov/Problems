#include <algorithm>
#include <vector>

// tags: two pointers, sliding window

// solution: two pointers, fast & slow
// complexity:
// run-time: O(n)
// space: O(1)
void moveZeroes(std::vector<int>& v)
{
    int slow = 0;
    int fast = 0;

    while (fast < v.size()) {
        // if fast is 0, do nothing

        // if fast is not 0, swap with slow
        if (v[fast] != 0) {
            // or swap
            std::swap(v[slow], v[fast]);
            // or overwrite: don't need v[fast]
            //v[slow] = v[fast];
            ++slow;
        }

        ++fast;
    }
}