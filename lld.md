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
- [Design Patterns](#design-patterns)
  - [Creational Patterns](#creational-patterns)
    - [Factory Method](#factory-method)
    - [Builder](#builder)
    - [Singleton](#singleton)
  - [Structural Patterns](#structural-patterns)
    - [Decorator](#decorator)
    - [Facade](#facade)
  - [Behavioral Patterns](#behavioral-patterns)
    - [Strategy](#strategy)
    - [Observer](#observer)
    - [State Machine](#state-machine)
- [Concurrency](#concurrency)
  - [Problem Types](#problem-types)
  - [Language Reference](#language-reference)
  - [Correctness](#correctness)
  - [Coordination](#coordination)
  - [Scarcity](#scarcity)

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

## Design Patterns

### Creational Patterns

#### Factory Method

* Use when callers shouldn’t care which concrete class gets created

#### Builder

* Use when an object has lots of optional fields or messy construction details

#### Singleton

* Use when you truly need one global instance (rare)

### Structural Patterns

#### Decorator

* Use when you need to layer optional behaviors at runtime without subclass explosion

#### Facade

* Use when you want to hide internal complexity behind a simple entry point

### Behavioral Patterns

#### Strategy

* Use when you're replacing if/else logic with interchangeable behaviors

#### Observer

* Use when multiple components need to react to a single event

#### State Machine

* Use when an object's behavior depends on its current state and transitions get messy

## Concurrency

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

