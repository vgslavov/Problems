#include <cstdlib>
#include <vector>
#include <unordered_map>

// number: 380
// section: array / string
// difficulty: medium 
// tags: array, hash table, math, design, randomized, top 150

// constraints
// -2^31 <= val <= 2^31 - 1
// At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
// There will be at least one element in the data structure when getRandom is called.

// solution: unordered map + vector
// complexity
// run-time: O(1) per op
// space: O(n)
class RandomizedSet {
public:
    RandomizedSet() = default;
    
    bool insert(int val) {
        auto it = d_val2idx.find(val);
        // found
        if (it != d_val2idx.end()) {
            return false;
        }

        d_idx2val.push_back(val);
        d_val2idx[val] = d_idx2val.size()-1;

        return true;
    }
    
    bool remove(int val) {
        auto it = d_val2idx.find(val);
        // not found
        if (it == d_val2idx.end()) {
            return false;
        }

        int idx = d_val2idx[val];
        d_val2idx.erase(val);

        // swap
        int lastElement = d_idx2val.back();
        d_idx2val[idx] = lastElement;
        d_idx2val.pop_back();

        if (idx < d_idx2val.size()) {
            d_val2idx[lastElement] = idx;
        }

        return true;
    }
    
    int getRandom() {
        auto it = d_idx2val.cbegin();
        int random = rand() % d_idx2val.size();
        std::advance(it, random);
        return *it;
    }

private:
    std::vector<int> d_idx2val;
    std::unordered_map<int, int> d_val2idx;
};

// Your RandomizedSet object will be instantiated and called as such:
RandomizedSet* obj = new RandomizedSet();
bool param_1 = obj->insert(1);
bool param_2 = obj->remove(3);
int param_3 = obj->getRandom();