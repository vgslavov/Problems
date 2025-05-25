#include <list>
#include <stdexcept>
#include <tuple>
#include <unordered_map>

// number: 146
// title: LRU Cache
// url: https://leetcode.com/problems/lru-cache/
// section: linked list
// difficulty: medium
// tags: hash table, linked list, design, doubly-linked list, top 150, meta,
// optiver, citadel

// constraints
// 1 <= capacity <= 3000
// 0 <= key <= 10^4
// 0 <= value <= 10^5
// At most 2 * 10^5 calls will be made to get and put.

// solution: unordered_map + list
// complexity
// run-time: O(1) for both put/get
// space: O(capacity)
#include <list>
#include <stdexcept>
#include <tuple>
#include <unordered_map>

class LRUCache {
public:
    LRUCache(int capacity)
    : d_capacity(capacity) {
        if (capacity <= 0) {
            throw std::invalid_argument("invalid capacity"); 
        }
    }

    int get(int key) {
        // refresh: make recently used if found
        return update(key, -1, false);
    }

    void put(int key, int value) {
        // update existing key if found
        if (update(key, value) != -1) {
            return;
        }

        // at capacity
        if (d_cache.size() == d_capacity) {
            int lruKey = std::get<0>(d_list.front());
            d_cache.erase(lruKey);
            d_list.pop_front();
        }

        // add new key
        d_list.push_back(std::make_tuple(key, value));

        // save an iterator to it
        d_cache[key] = std::prev(d_list.end());
    }

private:
    // refersh: make recently used if found & update
    int update(int key, int value, bool overwrite=true) {
        KeyListMap::iterator cacheIter = d_cache.find(key);
        if (cacheIter == d_cache.end()) {
            return -1;
        }

        ListTuples::iterator listIter = cacheIter->second;
        if (!overwrite) {
            value = std::get<1>(*listIter);
        }

        d_list.erase(listIter);
        d_list.push_back(std::tuple<int, int>(key, value));

        // get iter to last element, not end placeholder
        d_cache[key] = std::prev(d_list.end());

        return value;
    }

    // key, value tuples
    using ListTuples = std::list<std::tuple<int, int>>;
    // key: List iterator
    using KeyListMap = std::unordered_map<int, ListTuples::iterator>;
    KeyListMap d_cache;
    ListTuples d_list;
    int d_capacity;
};

// TODO: add unit tests

// Your LRUCache object will be instantiated and called as such:
int capacity = 2;
int key = 1;
LRUCache obj = LRUCache(capacity);
int param_1 = obj.get(key);
obj.put(key,value);