#include <vector>

// tags: two pointers

// solution: two pointers, fast & slow, same direction
// complexity:
// run-time: O(n)
// space: O(1)
int remove_duplicates(std::vector<int>& v)
{
    int slow = 0;
    int fast = 0;

    while (fast < v.size()) {
        // only advance slow pointer if we find a new unique element
        if (v[slow] != v[fast]) {
            // advance before assigning to avoid overwriting
            ++slow;
            v[slow] = v[fast];
        }

        // always advance fast pointer
        ++fast;
    }

    // length is index+1
    return slow+1;
}