#include <vector>
#include <stdexcept>

// number: 622
// title: Design Circular Queue
// url: https://leetcode.com/problems/design-circular-queue/
// section: citadel
// difficulty: medium
// tags: array, linked list, design, queue, citadel
//
// constraints
// 1 <= k <= 1000
// 0 <= value <= 1000
// At most 3000 calls will be made to enqueue, dequeue, front, rear, isempty, and
// isfull.

// solution: 2 vectors, using push_back
// complexity
// run-time: O(1) per op
// space: O(k)
template <typename T>
class MyCircularQueue {
public:
    MyCircularQueue(int k)
    : d_capacity(k)
    {
        if (k <= 0) {
            throw std::invalid_argument("invalid capacity");
        }

        // don't use reserve(), don't know how to split it b/w front & rear
    }

    // don't allow creation of queue with 0 capacity
    MyCircularQueue() = delete;

    // don't support copying
    MyCircularQueue(const MyCircularQueue&) = delete;
    MyCircularQueue& operator=(const MyCircularQueue&) = delete;

    // don't support moving
    MyCircularQueue(MyCircularQueue&&) = delete;
    MyCircularQueue& operator=(MyCircularQueue&&) = delete;

    bool enQueue(const T& value) {
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

    T Front() {
        // first check front!
        if (!d_front.empty()) {
            return d_front.front();
        } else if (!d_rear.empty()) {
            return d_rear.front();
        }

        throw std::length_error("empty queue");
    }

    T Rear() {
        // first check rear!
        if (!d_rear.empty()) {
            return d_rear.back();
        } else if(!d_front.empty()) {
            return d_front.back();
        }

        throw std::length_error("empty queue");
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
    std::vector<T> d_front;
    std::vector<T> d_rear;
    int d_capacity;
};

// solution: 1 vector w/o push_back
// + calc tail: (head + size-1) % capacity
// complexity
// run-time: O(1) per op
// space: O(k)
const size_t MAX_SIZE = 100;

template <typename T>
class MyCircularQueue2 {
public:
    MyCircularQueue2()
    : d_capacity(MAX_SIZE)
    , d_size(0)
    , d_head(0)
    {
        d_queue.reserve(d_capacity);
    }

    MyCircularQueue2(int k)
    : d_capacity(k)
    , d_size(0)
    , d_head(0)
    {
        if (k <= 0) {
            throw std::invalid_argument("invalid capacity");
        }

        // allocate memory
        d_queue.reserve(d_capacity);
    }

    // don't support copying
    MyCircularQueue2(const MyCircularQueue2&) = delete;
    MyCircularQueue2& operator=(const MyCircularQueue2&) = delete;

    // don't support moving
    MyCircularQueue2(MyCircularQueue2&&) = delete;
    MyCircularQueue2& operator=(MyCircularQueue2&&) = delete;

    bool enQueue(const T& value) {
        // TODO: increase capacity by doubling?
        if (isFull()) {
            return false;
        }

        // don't subtract 1: adding a new item!
        d_queue[(d_head + d_size) % d_capacity] = value;
        ++d_size;

        return true;
    }

    bool deQueue() {
        if (isEmpty()) {
            return false;
        }

        // make circular: if past end!
        d_head = (d_head + 1) % d_capacity;
        --d_size;

        return true;
    }

    T Front() {
        if (isEmpty()) {
            throw std::length_error("empty queue");
        }

        return d_queue[d_head];
    }

    T Rear() {
        if (isEmpty()) {
            throw std::length_error("empty queue");
        }

        // calc tail
        return d_queue[(d_head + d_size-1) % d_capacity];
    }

    bool isEmpty() { return d_size == 0; }

    bool isFull() { return d_size == d_capacity; }

private:
    std::vector<T> d_queue;
    size_t         d_capacity;
    size_t         d_size;
    size_t         d_head;
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
