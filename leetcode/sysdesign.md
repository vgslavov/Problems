# System Design

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [System Requirements](#system-requirements)
- [Non-functional Requirements](#non-functional-requirements)
  - [Availability](#availability)
  - [Scalability](#scalability)
  - [Performance](#performance)
  - [Durability](#durability)
  - [Consistency](#consistency)
  - [Maintainability](#maintainability)
  - [Security](#security)
  - [Cost](#cost)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## System Requirements

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

Source: [System Design Primer](https://github.com/donnemartin/system-design-primer?tab=readme-ov-file#appendix)

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

### Latencies

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