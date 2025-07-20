# System Design

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Concepts](#concepts)
  - [CAP](#cap)
    - [Consistency](#consistency)
    - [Availability](#availability)
    - [Levels of Consistency](#levels-of-consistency)
  - [Caching](#caching)
- [LeetCode Design Template](#leetcode-design-template)
  - [Feature Expectations](#feature-expectations)
  - [Estimations](#estimations)
  - [Design Goals](#design-goals)
  - [High Level Design](#high-level-design)
  - [Deep Dive](#deep-dive)
  - [Justify](#justify)
- [Hello Interview Design Template](#hello-interview-design-template)
  - [Requirements](#requirements)
  - [Core Entities](#core-entities)
  - [API or System Interface](#api-or-system-interface)
  - [Data Flow](#data-flow)
  - [High-Level Design](#high-level-design)
  - [Deep Dive](#deep-dive-1)
- [System Requirements](#system-requirements)
- [Non-functional Requirements](#non-functional-requirements)
  - [Availability](#availability-1)
  - [Scalability](#scalability)
  - [Performance](#performance)
  - [Durability](#durability)
  - [Consistency](#consistency-1)
  - [Maintainability](#maintainability)
  - [Security](#security)
  - [Cost](#cost)
- [Appendix](#appendix)
  - [Powers of 2](#powers-of-2)
  - [Powers of 10](#powers-of-10)
  - [Modern Hardware Limits](#modern-hardware-limits)
  - [Storage](#storage)
  - [Latencies](#latencies)
  - [Formulas](#formulas)
  - [Terminology](#terminology)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

Source:
* [Hello Interview: System Design](https://www.hellointerview.com/learn/system-design/)

### CAP

> "Does every read need to read the most recent write?" If the answer is yes, you need to prioritize *consistency*. If the answer is no, you can prioritize *availability*.

1. **Consistency**: All nodes see the same data at the same time.
2. **Availability**: Every request to a non-failing node receives a response.
3. **Partition Tolerance**: The system continues to operate despite arbitrary message loss or failure of part of the system

Real-world systems frequently need both availability and consistency - just for different features:
* strong consistency to prevent double-booking
* eventual consistency to see event description

#### Consistency

* **Distributed Transactions**: Ensuring multiple data stores (like cache and database) remain in sync through two-phase commit protocols.
* **Single-Node Solutions**: Using a single database instance to avoid propagation issues entirely.
* **Technology Choices**
    * Traditional RDBMS (PostgresSQL, MySQL)
    * Google Spanner
    * DynamoDB (in strong consistency mode)

#### Availability

* **Multiple Replicas**: Scaling to additional read replicas with asynchronous replication, allowing reads to be served from any replica.
* **Change Data Capture (CDC)**: Using CDC to track changes in the primary database and propagate them asynchronously to replicas, caches, and other systems.
* **Technology Choices**
    * Cassandra
    * DynamoDB (in multiple AZ configuration)
    * Redis clusters

#### Levels of Consistency

* **Strong Consistency**: All reads reflect the most recent write.
* **Causal Consistency**: Related events appear in the same order to all users.
* **Read-your-own-writes Consistency**: Users always see their own updates immediately, though other users might see older versions.
* **Eventual Consistency**: The system will become consistent over time but may temporarily have inconsistencies.

### Caching

* Goals
    * Save aggregated metrics
    * Reduce # of db queries
    * Speed up expensive queries
* Eviction policies
    * Least Recently Used (LRU): Evicts the least recently accessed items first.
    * First In, First Out (FIFO): Evicts items in the order they were added.
    * Least Frequently Used (LFU): Removes items that are least frequently accessed.
* Cache invalidation strategy
* Cache write strategy
    * Write-Through Cache: Writes data to both the cache and the underlying datastore simultaneously. Ensures consistency but can be slower for write operations.
    * Write-Around Cache: Writes data directly to the datastore, bypassing the cache. This can minimize cache pollution but might increase data fetch times on subsequent reads.
    * Write-Back Cache: Writes data to the cache and then asynchronously writes the data to the datastore. This can be faster for write operations but can lead to data loss if the cache fails before the data is written to the datastore.


## LeetCode Design Template

Source: [LeetCode: My System Design Template](https://leetcode.com/discuss/post/229177/my-system-design-template-by-topcat-vtk2/)

### Feature Expectations
[5 min]

1. Use cases
2. Out of scope
3. Who will use
4. How many will use
5. Usage patterns

### Estimations
[5 min]

1. Throughput (QPS for read and write queries)
2. Latency expected from the system (for read and write queries)
3. Read/Write ratio (typical: 10:1 -> 100:1)
4. Traffic estimates
    - Write (QPS, Volume of data)
    - Read  (QPS, Volume of data)
5. Storage estimates
6. Memory estimates
    - If we are using a cache, what is the kind of data we want to store in cache
    - How much RAM and how many machines do we need for us to achieve this ?
    - Amount of data you want to store in disk/ssd

### Design Goals
[5 min]

1. Latency and Throughput requirements
2. Consistency vs Availability
    * Weak/strong/eventual => consistency
    * Failover/replication => availability


### High Level Design
[5-10 min]

1. APIs for Read/Write scenarios for crucial components
2. Database schema
3. Basic algorithm
4. High level design for Read/Write scenario

### Deep Dive
[15-20 min]

1. Scaling the algorithm
2. Scaling individual components: 
    - Availability, Consistency and Scale story for each component
    - Consistency and availability patterns
3. Think about the following components, how they would fit in and how it would help
    * DNS
    * CDN [Push vs Pull]
    * Load Balancers [Active-Passive, Active-Active, Layer 4, Layer 7]
    * Reverse Proxy
    * Application layer scaling [Microservices, Service Discovery]
    * DB [RDBMS, NoSQL]
        - RDBMS 
            - Master-slave, Master-master, Federation, Sharding, Denormalization, SQL Tuning
        - NoSQL
            - Key-Value, Wide-Column, Graph, Document
            ```
            Fast-lookups:
            -------------
            RAM  [Bounded size] => Redis, Memcached
            AP [Unbounded size] => Cassandra, RIAK, Voldemort
            CP [Unbounded size] => HBase, MongoDB, Couchbase, DynamoDB
            ```
    * Caches
        - Client caching, CDN caching, Webserver caching, Database caching, Application caching, Cache @Query level, Cache @Object level
        - Eviction policies
            - Cache aside
                * Look for entry in cache, resulting in a cache miss
                * Load entry from the database
                * Add entry to cache
                * Return entry
            - Write through
                * Application adds/updates entry in cache
                * Cache synchronously writes entry to data store
                * Return
            - Write behind
                * Add/update entry in cache
                * Add event to queue
                * Return
                * Asynchronously write entry to the data store, improving write performance
            - Refresh ahead
    * Asynchronism
        - Message queues
        - Task queues
        - Back pressure
    * Communication
        - TCP
        - UDP
        - REST
        - RPC

### Justify
[5 min]

1. Throughput of each layer
2. Latency caused between each layer
3. Overall latency justification

## Hello Interview Design Template

### Requirements
[5 min]

1. Functional (*features* of system)
2. Non-functional (*qualities* of system)
3. Capacity estimations (skip for later)

### Core Entities
[2 min]

### API or System Interface
[5 min]

### Data Flow
[5 min]

Optional

### High-Level Design
[10-15min]

### Deep Dive
[10 min]

## System Requirements

Source: [LeetCode: System Design for Interviews and Beyond](https://leetcode.com/explore/featured/card/system-design-for-interviews-and-beyond/)

* functional
    * define behavior: what a system is supposed to do
    * example: exchange messages
    * *who* is going to use the system?
    * *how* are they going to use it?
* non-functional
    * define qualities: how a system is supposed to behave
    * example: scalable, highly available, fast

## Non-functional Requirements

* count-based: success ratio of requests
* time-based: system uptime

### Availability

System uptime, the percentage of time the system has been working and available.

* high availability: small downtime
* SLI & SLO & SLA
* fault tolerance
    * close to 0 downtime
* resilience ~ fault tolerance
    * ability to quickly recover from failures
* reliability
    * high availability + correctness + time

### Scalability

The property of a system to handle a growing load.

* vertical scaling
* horizontal scaling
* autoscaling
* scalability vs elasticity
    * scalability is required for elasticity
    * scalability: long-term, strategic needs
    * elasticity: short-term, tactical needs

### Performance

The *time* required to process something and/or the *rate* at which something is
processed.

* latency
* percentiles
* throughput
* bandwidth

### Durability

Once data is submitted to the system, it is not lost.

* backup
* RAID
* replication
* data corruption & checksum

### Consistency

Consistency of data across distributed copies.

* strong consistency
* weak consistency
* consistency model
* linearizability
* CAP
* eventual consistency
* monotonic reads
* read-your-writes
* consistent prefix reads

### Maintainability

The ease with which a product can be maintained.

* failure modes & mitigation
* monitoring
* testing
* deployment

### Security

Degree to which the system protects against threats.

* CIA triad
* identity and permissions management
* infrastructure protection
* data proctection

### Cost

How to design systems with the most effective use of resources.

* engineering cost
* maintenance cost
* hardware cost
* software cost

## Appendix

* Sources
    * [System Design Primer](https://github.com/donnemartin/system-design-primer?tab=readme-ov-file#appendix)
    * [What is Scalability Anyway](https://brooker.co.za/blog/2024/01/18/scalability.html)

### Powers of 2

```
Power           Exact Value         Approx Value        Bytes
---------------------------------------------------------------
7                             128
8                             256
10                           1024   1 thousand           1 KB
16                         65,536                       64 KB
20                      1,048,576   1 million            1 MB
30                  1,073,741,824   1 billion            1 GB
32                  4,294,967,296                        4 GB
40              1,099,511,627,776   1 trillion           1 TB
```

### Powers of 10

Source: [Hello Interview: Mastering Estimation](https://www.hellointerview.com/blog/mastering-estimation)

```
Power of 1000	Number	        Prefix
(1000^x)
----------------------------------------
0	            Unit	
1	            Thousand	    Kilo
2	            Million	        Mega
3	            Billion	        Giga
4	            Trillion	    Tera
5	            Quadrillion	    Peta
```

### Modern Hardware Limits

* In 2025,
    * Single databases can handle terabytes of data
    * Caches can hold entire datasets in memory
    * Message queues are fast enough for synchronous flows (as long as there is no backlog!)
    * Application servers have enough memory for significant local optimization
* 1st bottleneck: CPU utilization, not memory capacity
    * CPU > memory > network
* network latency in same cloud region: 1-2ms

|Component|Key Metrics|Scale Triggers|
|---------|-----------|--------------|
|Caching|~1ms latency|Hit rate < 80%|
||100k+ operations/second|Latency > 1ms|
||Memory-bound (up to 1TB)|Memory usage > 80%|
|||Cache churn/thrashing|
|Databases|Up to 50k transactions/second|Write throughput > 10k TPS|
||Sub-5ms read latency (cached)|Read latency > 5ms uncached|
||64 TiB+ storage capacity|Geographic distribution needs|
|App Servers|100k+ concurrent connections|CPU > 70% utilization|
||8-64 cores @ 2-4 GHz|Response latency > SLA|
||64-512GB RAM standard, up to 2TB|Connections near 100k/instance|
|||Memory > 80%|
|Message Queues|Up to 1 million msgs/sec per broker|Throughput near 800k msgs/sec|
||Sub-5ms end-to-end latency|Partition count ~200k per cluster|
||Up to 50TB storage|Growing consumer lag|

### Storage

```
Item	                    Size
----------------------------------------
A two-hour movie	        1gb
A small book of plain text	1mb
A high-resolution photo	    1mb
A medium-resolution image (or a site layout graphic)	100kb
```

### Latencies

* HDD IOPS: 120

```
Latency Comparison Numbers
--------------------------
L1 cache reference                           0.5 ns
Branch mispredict                            5   ns
L2 cache reference                           7   ns                      14x L1 cache
Mutex lock/unlock                           25   ns
Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
Compress 1K bytes with Zippy            10,000   ns       10 µs
Send 1 KB bytes over 1 Gbps network     10,000   ns       10 µs
Read 4 KB randomly from SSD*           150,000   ns      150 µs          ~1GB/sec SSD
Read 1 MB sequentially from memory     250,000   ns      250 µs
Round trip within same datacenter      500,000   ns      500 µs
Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 µs    1 ms  ~1GB/sec SSD, 4X memory
HDD seek                            10,000,000   ns   10,000 µs   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from 1 Gbps  10,000,000   ns   10,000 µs   10 ms  40x memory, 10X SSD
Read 1 MB sequentially from HDD     30,000,000   ns   30,000 µs   30 ms 120x memory, 30X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 µs  150 ms

Notes
-----
1 ns = 10^-9 seconds
1 µs = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 µs = 1,000,000 ns
```

```
L1 cache reference ......................... 0.5 ns
Branch mispredict ............................ 5 ns
L2 cache reference ........................... 7 ns
Mutex lock/unlock ........................... 25 ns
Main memory reference ...................... 100 ns
Compress 1K bytes with Zippy ............. 3,000 ns  =   3 µs
Send 2K bytes over 1 Gbps network ....... 20,000 ns  =  20 µs
SSD random read ........................ 150,000 ns  = 150 µs
Read 1 MB sequentially from memory ..... 250,000 ns  = 250 µs
Round trip within same datacenter ...... 500,000 ns  = 0.5 ms
Read 1 MB sequentially from SSD* ..... 1,000,000 ns  =   1 ms
Disk seek ........................... 10,000,000 ns  =  10 ms
Read 1 MB sequentially from disk .... 20,000,000 ns  =  20 ms
Send packet CA->Netherlands->CA .... 150,000,000 ns  = 150 ms
```

### Formulas

```
max latency = (transaction time / number of threads) * queue length
queue length = max latency / (transaction time / number of threads)
```

If queue is unbounded, latency increases. To set max response time, limit queue length.

### Terminology

* linearizability: all nodes reflect the most recent write operation
* scalable: a system is scalable in the range where the cost of adding incremental work is approximately constant
* IOPS: I/O per second
* WPS: writes per second