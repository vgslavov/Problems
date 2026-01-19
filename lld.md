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
    * `std::lock_guard` is a RAII wrapper for `std::mutex`
    ```cpp
    std::mutex mtx;
    {
        std::lock_guard<std::mutex> lock(mtx);
        // Only one thread can be in this critical section at a time
        balance += amount;
    }
    ```
    * `std::unique_lock` is a more flexible version of `std::lock_guard`
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

### Coordination

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