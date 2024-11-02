#include <vector>

// number: 303
// section: assessments
// difficulty: easy
// tags: array, design, prefix sum, meta

// constraints
// 1 <= nums.length <= 10^4
// -10^5 <= nums[i] <= 10^5
// 0 <= left <= right < nums.length
// At most 10^4 calls will be made to sum_range.

// solution: prefix sum
// complexity
// run-time: O(n)
// space: O(n)
class NumArray {
public:
    NumArray(const vector<int>& nums)
    : d_nums(nums)
    {
        calcPrefixSum();
    }

    int sumRange(int left, int right) {
        return d_prefixSum[right]-d_prefixSum[left]+d_nums[left];
    }

private:
    void calcPrefixSum() {
        if (d_nums.empty()) {
            return;
        }

        d_prefixSum.push_back(d_nums[0]);

        for (size_t i = 1; i != d_nums.size(); ++i) {
            d_prefixSum.push_back(d_prefixSum.back() + d_nums[i]);
        }
    }

    std::vector<int> d_nums;
    std::vector<int> d_prefixSum;
};

// Your NumArray object will be instantiated and called as such:
NumArray* obj = new NumArray(nums);
int param_1 = obj->sumRange(left,right);
