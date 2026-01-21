# Low-Level Design

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [References](#references)
- [Design Principles](#design-principles)
- [OOP Concepts](#oop-concepts)
  - [Encapsulation](#encapsulation)
  - [Abstraction](#abstraction)
  - [Composition](#composition)
  - [Inheritance](#inheritance)
  - [Polymorphism](#polymorphism)
- [Concurrency](#concurrency)
  - [APIs](#apis)
  - [Problem Types](#problem-types)
  - [Language Reference](#language-reference)
  - [Correctness](#correctness)
    - [Course-Grained Locking](#course-grained-locking)
    - [Fine-Grained Locking](#fine-grained-locking)
    - [Atomic Variables](#atomic-variables)
    - [Thread Confinement / Shared Nothing / Isolation](#thread-confinement--shared-nothing--isolation)
    - [Common Bugs](#common-bugs)
  - [Coordination](#coordination)
  - [Scarcity](#scarcity)
    - [Semaphores](#semaphores)
    - [Resource Pooling / Blocking Queues](#resource-pooling--blocking-queues)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## References

* [Hello Interview: Low Level Design](https://www.hellointerview.com/learn/low-level-design/)

## Design Principles

## OOP Concepts

### Encapsulation

### Abstraction

### Composition

### Inheritance

### Polymorphism

## Concurrency

### APIs

* **Atomics**: thread-safe operations on a single variable w/o locks
```cpp
#include <atomic>

std::atomic<int> counter(0);
counter++;  // Thread-safe increment
```
* **Locks (Mutexes)**: ensure only one thread can access a resource at a time
    * `std::lock_guard<std::mutex>` is a RAII *wrapper* of `std::mutex`
    * instead of manually calling `mutex.lock()` and `mutex.unlock()`
    * unlocks automatically when the scope is exited
    ```cpp
    std::mutex mtx;
    {
        std::lock_guard<std::mutex> lock(mtx);
        // Only one thread can be in this critical section at a time
        balance += amount;
    }
    ```
    * `std::shared_lock`: for read access, multiple threads allowed
    * `std::unique_lock`: for write access, only one thread allowed
        * a more flexible version of `std::lock_guard`
        * can be used to temporarily release the lock
        * can be used to wait for a condition to be met
* **Semaphores**: counting locks
```cpp
std::counting_semaphore<5> permits(5);  // Allow 5 concurrent operations
permits.acquire();  // Block if no permits available
try {
    doWork();
} catch (...) {
    permits.release();
    throw;
}
permits.release();  // Always release
```
* **Condition Variables**: wait for a condition to be met
```cpp
std::mutex mtx;
std::condition_variable cv;

std::unique_lock<std::mutex> lock(mtx);
cv.wait(lock, [] { return condition; });  // Release lock and sleep
// Condition is now true
```
* **Blocking Queues**: combine a queue with a condition variable
```cpp
// C++ standard library doesn't include a blocking queue
// Typically implemented using mutex + condition_variable
// or use a third-party library like Intel TBB

template<typename T>
class BlockingQueue {
    std::queue<T> queue;
    std::mutex mtx;
    std::condition_variable cv;
public:
    void put(T item);   // Blocks if queue is full
    T take();           // Blocks if queue is empty
};
```

### Problem Types

| Problem Type  | What Breaks                          | Solutions                                   | Common Problems                                  |
|---------------|--------------------------------------|---------------------------------------------|--------------------------------------------------|
| Correctness   | Shared state is updated concurrently | Locks, atomics, thread confinement           | Check-then-act, read-modify-write                |
| Coordination  | Threads need ordering or handoff      | Blocking queues, actors, event loops         | Async request processing, bursty traffic         |
| Scarcity      | Resources are limited                 | Semaphores, resource pools                   | Concurrent op limits, resource consumption, object reuse |

### Language Reference

|Concept|Python|C++|
|-------|------|---|
|Thread|`threading.Thread`|`std::thread`|
|Lock/Mutex|`threading.Lock`|`std::mutex`|
|Read-write Lock|N/A (3rd party)|`mutable std::shared_mutex`: read: `std::shared_lock`, write: `std::unique_lock`|
|Condition Variable|`threading.Condition`|`std::condition_variable`|
|Semaphore|`threading.Semaphore`|`std::counting_semaphore`|
|Blocking Queue|`queue.Queue`|manual|
|Atomic Integer|N/A (use `threading.Lock`)|`std::atomic`|
|Concurrent Map|N/A (GIL)|Intel TBB: `tbb::concurrent_hash_map`|

### Correctness

#### Course-Grained Locking

* protects all related state with one lock
* `std::lock_guard<std::mutex>`
* mistakes
    * releasing the lock too early
    * using different lock objects for operations that need to be atomic together
* all operations that maintain an invariant must be protected by the same lock
* if you hold the lock during the check, you must still hold it during the update
* read/write locks (shared-exclusive locks): when `reads >> writes`
```cpp
// mutable: lock can be used in const methods!
mutable std::shared_mutex rwMutex;

// multiple threads can read at the same time
std::shared_lock<std::shared_mutex> readLock(rwMutex);

// only one thread can write at a time
std::unique_lock<std::shared_mutex> writeLock(rwMutex);
```

#### Fine-Grained Locking

* allows concurrent access to independent resources while protecting related ones
* scales better than course-grained locking for large number of threads/resources
* use when processing machine-generated data (e.g., logs, metrics, events)
```cpp
std::mutex locksMutex;

// unique_ptr to mutex not lock_guard!
std::unordered_map<std::string, std::unique_ptr<std::mutex>> seatLocks;

// create lock_guard from mutex on the fly!
std::lock_guard<std::mutex> lock(getLock(seatId));
```
* mistakes
    * not acquiring locks in the correct/consistent order to prevent deadlocks
    * not clearing dynamically allocated locks not in use

#### Atomic Variables

* work for single variables but fail for multi-field invariants
* use special CPU instructions to perform read-modify-write operations in a single, uninterruptible step w/o needing a lock
* CAS (Compare-And-Swap)
    * an atomic instruction that compares the value of a memory location with an expected value
    * if they are the same, it replaces the value with a new one
    * if they are different, it does nothing
* with a regular integer, incrementing is unsafe because increment operations are actually three steps (read, add, write) that can interleave b/w threads
* faster & simpler than locks
```cpp
std::atomic<int> bookedCount{0};
// increment by 1
bookedCount.fetch_add(1);
// or use the increment operator
//++bookedCount;
// read
bookedCount.load();
```
* optimistic concurrency control
    * try to update the value, if it fails, retry
    * `compare_exchange_strong`: stronger, more reliable, but may fail spuriously
    * `compare_exchange_weak`: weaker, may fail spuriously, but faster
    ```cpp
    std::atomic<int> bookedCount{0};
    // try to increment by 1
    if (bookedCount.compare_exchange_strong(0, 1)) {
    // use in loop to handle spurious failures
    //if (bookedCount.compare_exchange_weak(0, 1)) {
        // success
    } else {
        // retry
    }
    ```
* mistakes
    * using atomic for multiple variables that need to be updated together
    * not using atomic variables for counters/flags/stats only

#### Thread Confinement / Shared Nothing / Isolation

* eliminates concurrency entirely for related data
* avoid sharing data between threads in the first place
* trades synchronization complexity for architecture complexity
* partition data and assign to different threads
* overkill unless need scalability

#### Common Bugs

* check-then-act
    * check a condition, make a decision based on that check, then act on it
    * another thread invalidates the check between when you read it and when you act on it
* read-modify-write
    * when two threads read the same value, both compute from it, and both write back, causing one update to get lost

### Coordination

#### Common Bugs

* busy-waiting: repeatedly check a condition without sleeping
* sleep-polling: sleep for a short time, then check the condition again

#### Goals

1. Efficient waiting — consumers should sleep when there's no work, waking immediately when work arrives
2. Backpressure — producers should slow down when consumers can't keep up, preventing memory exhaustion
3. Thread safety — the coordination mechanism itself must handle concurrent access without corruption

#### Shared State

* wait/notify (condition variables)
    * `wait`
        * thread releases the lock and goes to sleep.
        * thread stops consuming CPU entirely: paused until explicitly woken
    ```cpp
    {
        std::mutex mutex;
        // not a lock_guard: wait needs to unlock
        std::unique_lock<std::mutex> lock(mutex);
        std::condition_variable cv;

        // recheck condition after waking up in case another thread modified it
        while (!conditionIsMet()) {
            cv.wait(lock);  // Releases lock, sleeps until notified
        }
        doWork();

        // wake up all threads to prevent a deadlock:
        // if you wake only one, you may wake up another consumer instead of producer
        cv.notify_all();
    }
    ```
* blocking queues (semaphore with N permits)
```cpp
#include <queue>
#include <mutex>
#include <condition_variable>
#include <functional>

class TaskScheduler {
    std::queue<std::function<void()>> queue_;
    std::mutex mutex_;
    std::condition_variable not_empty_;
    std::condition_variable not_full_;
    static constexpr size_t MAX_SIZE = 1000;

public:
    void submitTask(std::function<void()> task) {
        std::unique_lock<std::mutex> lock(mutex_);
        not_full_.wait(lock, [this] { return queue_.size() < MAX_SIZE; });
        queue_.push(std::move(task));
        not_empty_.notify_one();
    }

    void workerLoop() {
        while (true) {
            std::function<void()> task;
            {
                std::unique_lock<std::mutex> lock(mutex_);
                not_empty_.wait(lock, [this] { return !queue_.empty(); });
                task = std::move(queue_.front());
                queue_.pop();
                not_full_.notify_one();
            }
            task();
        }
    }
};
```
* common mistakes
    * creating an unbounded queue: set capacity
        * **block producers** if queue is full w/ `put`
        * **timeout & reject** `offer(timeout)`
        * **drop & log** `offer` without timeout, returns false
    * not graceful shutdown
        * interrupt the worker thread: `throw`
        * use poll w/ timeout: `wait_for`
        * use poison pill: special task to signal shutdown

#### Message Passing

* actor model: an object w/ a mailbox & message handler
* actor pulls messages from mailbox 1 at-a-time
* internal state is thread-confined
* challenges
    * mailbox overlfow
    * messsage ordering
    * debugging
    * request-response patterns

#### Use Cases

* process requests asynchronously
* handle bursty traffic

### Scarcity

* managing limited resources
* `N` threads, `M` resources, `M < N`

#### Semaphores

* limit how many threads can hold a resource simultaneously
```cpp
#include <semaphore>

class APIClient {
private:
    std::counting_semaphore<5> requestPermits{5};     // max 5 concurrent requests

public:
    Response makeRequest(const std::string& endpoint) {
        requestPermits.acquire();                     // increment counter
        try {
            auto response = httpClient.get(endpoint);
            requestPermits.release();                  // decrement counter
            return response;
        } catch (...) {
            requestPermits.release();                  // decrement counter!
            throw;
        }
    }
};
```

#### Resource Pooling / Blocking Queues

* get actual resource objects, not just permission
* C++ doesn't have a built-in blocking queue, so we need to implement one
```cpp
#include <queue>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <stdexcept>

class Connection {
public:
    void execute(const std::string& query) {
        // execute query
    }
};

class ConnectionPool {
private:
    std::queue<Connection*> d_availableConnections;     // container adapter using deque
    std::mutex d_mtx;
    std::condition_variable d_cv;
    std::chrono::milliseconds d_timeout{1000};

public:
    // limit number of maximum connections!
    ConnectionPool(int poolSize, std::chrono::milliseconds timeout)
    : d_timeout(timeout) {
        // create poolSize connections
        for (int i = 0; i < poolSize; i++) {
            d_availableConnections.push(createNewConnection());
        }
    }

    Connection* acquire() {
        // 1. acquire *unique* lock, not lock_guard!
        // wait_for/wait requires unique_lock to temporarily release the lock!
        std::unique_lock<std::mutex> lock(d_mtx);

        // 2. block until predicate is true
        // w/ timeout, wait for timeout or predicate is true
        if (!d_cv.wait_for(lock, d_timeout, [this] { return !d_availableConnections.empty(); })) {
            throw std::runtime_error("No connection available within timeout");
        }

        // w/o timeout, wait forever!
        //d_cv.wait(lock, [this] { return !d_availableConnections.empty(); });

        // 3. get connection from front of queue
        Connection* conn = d_availableConnections.front();

        // 4. remove connection from queue
        d_availableConnections.pop();

        return conn;
    }

    void release(Connection* conn) {
        // 1. acquire lock
        // lock_guard is enough because we don't have to relock before returning!
        std::lock_guard<std::mutex> lock(d_mtx);

        // 2. add connection to back of queue
        d_availableConnections.push(conn);

        // 3. notify one waiting thread
        d_cv.notify_one();
    }

    void executeQuery(const std::string& query) {
        // 1. acquire connection from pool
        Connection* conn = acquire();

        // 2. execute query
        try {
            conn->execute(query);

            // 3. release connection back to pool
            release(conn);
        } catch (...) {
            // 3. release connection back to pool!
            release(conn);
            throw;
        }
    }
};
```

* Limit concurrent operations (semaphore with N permits)
    * rate-limited API calls
    * image processing pipeline
    * video transcoding
* Limit aggregate consumption (semaphore with permits = resource units)
    * bandwidth limiter
    * memory limiter
* Reuse expensive objects (blocking queue of actual objects)
    * database connections
    * GPU task scheduler
* Maximizing utilization
    * work stealing
        * handle uneven task distribution
        * replace single queue with multiple queues, one per worker
        * workers w/ empty queues steal from others
    * batching
        * amortizes coordination overhead
        * acquire 1 connection, write 100 rows, release
        * trade latency for throughput
            * individidual task time goes up
            * but total work per sec goes up as well
    * adaptive sizing
        * adjust pool capacity based on demand
        * complexity in tuning