#include <map>
#include <iostream>

// number: 362
// title: Design Hit Counter
// url: https://leetcode.com/problems/design-hit-counter/
// difficulty: medium
// tags: array, binary search, design, queue, data stream

// constraints:
// 1 <= timestamp <= 2 * 10^9
// All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing).
// At most 300 calls will be made to hit and getHits.

// solution: map + lower_bound/upper_bound
// complexity:
// run-time: O(log n) for hit, O(n) for getHits
// space: O(n)
class HitCounter {
public:
    HitCounter() = default;
    
    // TODO: remove timestamps older than 300 seconds
    void hit(int timestamp) {
        ++d_timestamp2count[timestamp];
    }
    
    int getHits(int timestamp) {
        int fromTime = timestamp > 300 ? timestamp-300+1 : 0;
        //std::cout << "fromTime: " << fromTime << std::endl;

        auto fromIter = d_timestamp2count.lower_bound(fromTime);
        //std::cout << "fromIter timestamp: " << fromIter->first << std::endl;

        if (fromIter == d_timestamp2count.end()) {
            return 0;
        }

        auto toIter = d_timestamp2count.upper_bound(timestamp);
        //std::cout << "toIter timestamp: " << toIter->first << std::endl;

        int ans = 0;

        while (fromIter != d_timestamp2count.end()) {
            ans += fromIter->second;
            ++fromIter;
        }

        return ans;
    }
private:
    std::map<int, int> d_timestamp2count;
};

// TODO: add unit tests & solve w/o upper_bound/lower_bound

int main() {
    // Your HitCounter object will be instantiated and called as such:
    HitCounter* obj = new HitCounter();
    int timestamp = 1;
    obj->hit(timestamp);
    int param_2 = obj->getHits(timestamp);
    return 0;
}