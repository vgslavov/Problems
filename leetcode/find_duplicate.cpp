#include <vector>

long int getBit(long int value, int index)
{
    return value & (1 << index);
}

long int setBit(long int value, int index)
{
    return value | (1 << index);
}

int findDuplicate(std::vector<int>& nums) {
    long int bitmap = 0;

    for (const auto& n: nums) {
        if (getBit(bitmap, n)) {
            return n;
        } else {
            bitmap = setBit(bitmap, n);
        }
    }

    return 0;
}

// TODO: add unit tests & fix overflow for:
// [13,46,8,11,20,17,40,13,13,13,14,1,13,36,48,41,13,13,13,13,45,13,28,42,13,10,15,22,13,13,13,13,23,9,6,13,47,49,16,13,13,39,35,13,32,29,13,25,30,13]