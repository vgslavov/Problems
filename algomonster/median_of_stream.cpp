#include <cstdlib>
#include <queue>

// tags: heap

// solution: min & max heaps
// complexity:
// run-time: (q*log q), where q is # of queries
// space: O(n)
class MedianOfStream {
public:
    void addNumber(double num)
    {
        // min heap contains the larger numbers
        if (!d_minHeap.empty() && num > d_minHeap.top()) {
            d_minHeap.push(num);
        } else {
            d_maxHeap.push(num);
        }

        balance();
    }

    double getMedian()
    {
        // evenly split
        if (d_minHeap.size() == d_maxHeap.size()) {
            // median is average of 2 middle values
            return (d_minHeap.top() + d_maxHeap.top()) / 2;
        } else if (d_minHeap.size() > d_maxHeap.size()) {
            return d_minHeap.top();
        } else {
            return d_maxHeap.top();
        }
    }

private:
    void balance()
    {
        if (std::abs(d_minHeap.size()-d_maxHeap.size()) <= 1) {
            return;
        }

        if (d_maxHeap.size() > d_minHeap.size()) {
            d_minHeap.push(d_maxHeap.top());
            d_maxHeap.pop();
        } else if (d_minHeap.size() > d_maxHeap.size()) {
            d_maxHeap.push(d_minHeap.top());
            d_minHeap.pop();
        }
    }

    // store numbers *larger* than median
    std::priority_queue<double, std::vector<double>, std::greater<double>> d_minHeap;
    // store numbers *smaller* than median
    std::priority_queue<double, std::vector<double>, std::less<double>> d_maxHeap;

    // invariant
    // d_maxHeap.top() <= median <= d.minHeap.top()
};