# Low-Level Design

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [References](#references)
- [Problem Types](#problem-types)
- [Language Reference](#language-reference)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## References

* [Hello Interview: Low Level Design](https://www.hellointerview.com/learn/low-level-design/)

## Problem Types

| Problem Type  | What Breaks                          | Solutions                                   | Common Problems                                  |
|---------------|--------------------------------------|---------------------------------------------|--------------------------------------------------|
| Correctness   | Shared state is updated concurrently | Locks, atomics, thread confinement           | Check-then-act, read-modify-write                |
| Coordination  | Threads need ordering or handoff      | Blocking queues, actors, event loops         | Async request processing, bursty traffic         |
| Scarcity      | Resources are limited                 | Semaphores, resource pools                   | Concurrent op limits, resource consumption, object reuse |

## Language Reference

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
