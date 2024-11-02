#include <vector>
#include <stdexcept>

// number: 622
// section: citadel
// difficulty: medium
// tags: array, linked list, design, queue, citadel
//
// constraints
// 1 <= k <= 1000
// 0 <= value <= 1000
// At most 3000 calls will be made to enqueue, dequeue, front, rear, isempty, and
// isfull.

// solution: 2 lists
// complexity
// run-time: O(1) per op
// space: O(k)
class MyCircularQueue {
public:
    MyCircularQueue(int k)
    : d_capacity(k)
    {
        if (k <= 0) {
            throw std::invalid_argument("invalid capacity");
        }
    }

    // don't allow creation of queue with 0 capacity
    MyCircularQueue() = delete;

    // don't support copying
    MyCircularQueue(const MyCircularQueue&) = delete;
    MyCircularQueue& operator=(const MyCircularQueue&) = delete;

    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }

        d_rear.push_back(value);
        return true;
    }

    bool deQueue() {
        if (isEmpty()) {
            return false;
        }

        if (!d_front.empty()) {
            d_front.erase(d_front.begin());
            return true;
        } else if (!d_rear.empty()) {
            d_rear.erase(d_rear.begin());
            return true;
        }

        return false;
    }

    int Front() {
        // first check front!
        if (!d_front.empty()) {
            return d_front.front();
        } else if (!d_rear.empty()) {
            return d_rear.front();
        } else {
            return -1;
        }

        return -1;
    }

    int Rear() {
        // first check rear!
        if (!d_rear.empty()) {
            return d_rear.back();
        } else if(!d_front.empty()) {
            return d_front.back();
        } else {
            return -1;
        }

        return -1;
    }

    bool isEmpty() {
        if (!d_front.empty() or !d_rear.empty()) {
            return false;
        }

        return true;
    }

    bool isFull() {
        if (d_front.size() + d_rear.size() >= d_capacity) {
            return true;
        }

        return false;
    }

private:
    std::vector<int> d_front;
    std::vector<int> d_rear;
    int d_capacity;
};

// TODO: solve using linked list & unit test

// Your MyCircularQueue object will be instantiated and called as such:
MyCircularQueue* obj = new MyCircularQueue(k);
bool param_1 = obj->enQueue(value);
bool param_2 = obj->deQueue();
int param_3 = obj->Front();
int param_4 = obj->Rear();
bool param_5 = obj->isEmpty();
bool param_6 = obj->isFull();
