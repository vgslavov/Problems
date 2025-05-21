#include <deque>

// number: 346
// title: Moving Average from Data Stream
// url: https://leetcode.com/problems/moving-average-from-data-stream/
// section: assessments
// difficulty: easy
// tags: array, design, queue, data stream, amazon

// constraints
// 1 <= size <= 1000
// -10^5 <= val <= 10^5
// At most 10^4 calls will be made to next.

// solution: deque
// complexity
// run-time: O(k)
// space: O(k)
class MovingAverage {
public:
    MovingAverage(int size)
    : d_size(size)
    , d_sum(0) {}

    double next(int val) {
        d_sum += val;

        if (d_queue.empty()) {
            d_queue.push_back(val);
            return val;
        }

        // at capacity, remove the oldest element
        if (d_queue.size() == d_size) {
            d_sum -= d_queue.front();
            d_queue.pop_front();
        }

        d_queue.push_back(val);
        return d_sum / d_queue.size();
    }

private:
    int d_size;
    double d_sum;
    std::deque<int> d_queue;
};

// Your MovingAverage object will be instantiated and called as such:
MovingAverage* obj = new MovingAverage(size);
double param_1 = obj->next(val);
