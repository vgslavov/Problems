#include <vector>
#include <unordered_map>

// number: 1570
// title: Dot Product of Two Sparse Vectors
// url: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
// section: meta
// difficulty: medium
// tags: array, hash table, two pointers, design, meta

// constraints
// n == nums1.length == nums2.length
// 1 <= n <= 10^5
// 0 <= nums1[i], nums2[i] <= 100

// solution: brute-force
// complexity
// run-time: O(n)
// space: O(1)
class SparseVector {
private:
    std::vector<int> d_nums;
public:
    
    SparseVector(const std::vector<int> &nums) {
        d_nums = nums;
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(const SparseVector& vec) {
        if (vec.d_nums.size() != d_nums.size()) {
            return 0;
        }

        int ans = 0;

        for (size_t i = 0; i != d_nums.size(); ++i) {
            ans += d_nums[i] * vec.d_nums[i];
        }

        return ans;
    }
};

// solution: unordered_map
// complexity
// run-time: O(n)
// space: O(1)
class SparseVector2 {
private:
    std::unordered_map<int, int> d_index2val;
public:
    
    SparseVector2(const std::vector<int> &nums) {
        for (size_t i = 0; i != nums.size(); ++i) {
            if (nums[i]) {
                d_index2val[i] = nums[i];
            }
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(const SparseVector2& vec) {
        int ans = 0;

        for (const auto & pair : d_index2val) {
            auto it = vec.d_index2val.find(pair.first);
            if (it == vec.d_index2val.end()) {
                continue;
            }

            ans += pair.second * it->second;
        }

        return ans;
    }
};

// Your SparseVector object will be instantiated and called as such:
SparseVector v1(nums1);
SparseVector v2(nums2);
int ans = v1.dotProduct(v2);