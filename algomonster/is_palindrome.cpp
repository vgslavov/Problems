#include <string>

// tags: two pointers

// solution: two pointers, opposite direction
// complexity:
// run-time: O(n)
// space: O(1)
bool isPalindrome(const std::string& s)
{
    int left = 0;
    int right = s.size()-1;

    while (left < right) {
        if (std::isalpha(s[left])) {
            ++left;
            continue;
        }

        if (std::isalpha(s[right])) {
            --right;
            continue;
        }

        if (std::tolower(s[left]) != std::tolower(s[right])) {
            return false;
        }

        ++left;
        --right;
    }

    return true;
}