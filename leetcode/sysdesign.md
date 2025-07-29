# System Design

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Sources](#sources)
- [Concepts](#concepts)
  - [Communication Protocols](#communication-protocols)
  - [API Types](#api-types)
    - [REST (Representational State Transfer)](#rest-representational-state-transfer)
    - [GraphQL](#graphql)
    - [RPC (Remote Procedure Call)](#rpc-remote-procedure-call)
    - [Patterns](#patterns)
  - [CAP](#cap)
    - [Consistency](#consistency)
    - [Availability](#availability)
    - [Partition Tolerance](#partition-tolerance)
    - [Levels of Consistency](#levels-of-consistency)
  - [ACID](#acid)
    - [Atomicity](#atomicity)
    - [Consistency](#consistency-1)
    - [Isolation](#isolation)
    - [Durability](#durability)
  - [SQL](#sql)
    - [Commands](#commands)
  - [Caching](#caching)
    - [Goals](#goals)
    - [Eviction Policies](#eviction-policies)
    - [Cache Invalidation Strategies](#cache-invalidation-strategies)
    - [Cache Write Strategies](#cache-write-strategies)
    - [Hot Keys](#hot-keys)
    - [High-Performant Caches](#high-performant-caches)
  - [Database Indexes](#database-indexes)
    - [B-Tree Indexes](#b-tree-indexes)
    - [LSM Trees](#lsm-trees)
    - [Hash Indexes](#hash-indexes)
    - [Geospatial Indexes](#geospatial-indexes)
    - [Inverted Indexes](#inverted-indexes)
    - [Index Optimizations](#index-optimizations)
- [Patterns](#patterns-1)
  - [Scaling Reads](#scaling-reads)
  - [Scaling Writes](#scaling-writes)
- [Key Technologies](#key-technologies)
  - [Redis](#redis)
    - [Data Structures](#data-structures)
    - [Cache](#cache)
    - [Distributed Lock](#distributed-lock)
    - [Leaderboard](#leaderboard)
    - [Rate Limiting](#rate-limiting)
    - [Proximity Search](#proximity-search)
    - [Event Sourcing](#event-sourcing)
    - [Pub/Sub](#pubsub)
    - [Limitations](#limitations)
  - [Kafka](#kafka)
    - [Terms](#terms)
    - [Design & Processes](#design--processes)
    - [Use Cases](#use-cases)
    - [Scalability](#scalability)
    - [Fault Tolerance & Durability](#fault-tolerance--durability)
    - [Handling Retries & Errors](#handling-retries--errors)
    - [Performance Optimizations](#performance-optimizations)
    - [Retention Policies](#retention-policies)
  - [PostgresSQL](#postgressql)
    - [Reads: Basic Indexing](#reads-basic-indexing)
    - [Reads: Beyond Basic Indexes](#reads-beyond-basic-indexes)
    - [Reads: Query Optimization Essentials](#reads-query-optimization-essentials)
    - [Reads: Practical Performance Limits](#reads-practical-performance-limits)
    - [Writes: Steps](#writes-steps)
    - [Writes: Throughput Limitations](#writes-throughput-limitations)
    - [Writes: Optimizations](#writes-optimizations)
    - [Replication](#replication)
    - [Transactions](#transactions)
    - [Use Cases](#use-cases-1)
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
  - [Scalability](#scalability-1)
  - [Performance](#performance)
  - [Durability](#durability-1)
  - [Consistency](#consistency-2)
  - [Maintainability](#maintainability)
  - [Security](#security)
  - [Cost](#cost)
- [Appendix](#appendix)
  - [Powers of 2](#powers-of-2)
  - [Powers of 10](#powers-of-10)
  - [Time](#time)
  - [Modern Hardware Limits](#modern-hardware-limits)
  - [Storage](#storage)
  - [Latencies](#latencies)
  - [Formulas](#formulas)
  - [Terminology](#terminology)
  - [HTTP Codes](#http-codes)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Sources

* [Distributed Locks with Redis](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/)
* [Hello Interview: Mastering Estimation](https://www.hellointerview.com/blog/mastering-estimation)
* [Hello Interview: System Design](https://www.hellointerview.com/learn/system-design/)
* [Latency Numbers Every Programmer Should Know](https://gist.github.com/jboner/2841832)
* [LeetCode: My System Design Template](https://leetcode.com/discuss/post/229177/my-system-design-template-by-topcat-vtk2/)
* [LeetCode: System Design for Interviews and Beyond](https://leetcode.com/explore/featured/card/system-design-for-interviews-and-beyond/)
* [PG's Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)
* [System Design Primer](https://github.com/donnemartin/system-design-primer/)
* [What is Scalability Anyway](https://brooker.co.za/blog/2024/01/18/scalability.html)

## Concepts

### Communication Protocols

In order of increasing complexity and functionality:

1. REST
    * Request -> Response
    * stateless!
2. Long Polling
    * client sends req to server
    * server holds it open until data is available
    * client keeps sending req to keep the connection open
    * works with load balancers
3. SSE (Server-Side Events)
    * similar to long polling
    * more efficient for unidirectional comm. from server to client
    * over single, long-lived HTTP connection
4. WebSockets
    * for real-time, bi-directional communication b/w client & server
    * have to maintain connection
    * challenging to maintain across load balancers

### API Types

#### REST (Representational State Transfer)

* default choice
* JSON-over-HTTP
* resources represent *things* not actions
* resources are the [entities](#core-entities)
* always use plural nouns!
```
GET /events                    # Get all events
GET /events/{id}               # Get a specific event
GET /events/{id}/tickets       # Get available tickets for an event
POST /bookings                 # Create a new booking
GET /bookings/{id}             # Get a specific booking
```
* verbs
    * `DELETE`: Delete an existing resource
        * idempotent
    * `GET`: Read an existing resource (like `SELECT`)
        * safe
        * idempotent
    * `PATCH`: Submit partial modification to a resource (like `UPDATE`)
        * idempotent
    * `POST`: Create a *new* resource (like `INSERT`)
        * not safe
        * not idempotent
    * `PUT`: Update an existing resource (like `UPDATE`)
        * idempotent
* arguments
    * path parameters: `/events/123`
        * use nested resources: `/events/{id}/tickets`
            * to specify parent-child relationship
            * when value is required
    * query parameters: `/events?page=2&limit=20`
        * when filter is optional
    * request body

#### GraphQL

* consolidates resource endpoints into single one
* use for diverse clients with different data needs
* use to avoid over/under fetching

#### RPC (Remote Procedure Call)

* *action*-oriented (instead of resource-oriented)
* like calling a procedure on a server as if it's local
* faster than REST
* compare to REST
```
// Instead of GET /events/123/tickets
getAvailableTickets(eventId: "123", section: "VIP")
```
* examples
    * gRPC: protobuf to serialize + HTTP/2 to transport
        * much faster than REST
        * great for service-to-service
    * Apache Thrift
* use cases
    * performance is critical: binary serialization
    * type safety matters
    * service-to-service communication
    * streaming is needed

#### Patterns

* pagination
    * offset-based
        * `/events?offset=20&limit=10`
        * simpler but not for large datasets
    * cursor-based
        * `/events?cursor=cmd9atj3p000007ky19w1dpy2&limit=10`
        * use pointer to specific record: get cursor from previous response
* versioning strategies
    * URL versioning: `/v2/events`
    * (HTTP) header versioning: `API-Version: 2`
* security considerations
    * authenticaion: verifies identity
    * authorization: verifies permissions
    * API keys
        * long, randomly generated strings acting like passwords for apps
        * for service-to-service communication
    * JWT (JSON Web Tokens)
        * signed tokens
        * contains user ID, permissions, expire time
        * for client-facing services to establish a user session
    * Role-Based Access Control (RBAC)
    * rate limiting & throttling
        * per-user limits: 1000 reqs/hour per auth. users
        * per-IP limits: 100 reqs/hour for unauth. users
        * endpoint-specific limits: 10 booking attempts per min

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
* **Change Data Capture (CDC)**: Using CDC to track changes in the primary database and propagate them *asynchronously* to replicas, caches, and other systems.
* **Technology Choices**
    * Cassandra
    * DynamoDB (in multiple AZ configuration)
    * Redis clusters

#### Partition Tolerance

* required in a *distributed* system

#### Levels of Consistency

* **Strong Consistency**: All reads reflect the most recent write.
* **Causal Consistency**: Related events appear in the same order to all users.
* **Read-your-own-writes Consistency**: Users always see their own updates immediately, though other users might see older versions.
* **Eventual Consistency**: The system will become consistent over time but may temporarily have inconsistencies.

### ACID

#### Atomicity

* all or nothing
* transactions
* prevent partial failures: roll back changes if failure

####  Consistency

* data integrity
* follow defined rules & constraints (e.g. value can't be negative)
* != C in CAP (always return correct result)

#### Isolation

* concurrent transactions
* dirty read
    * A transaction reads data written by a concurrent *uncommitted* transaction
* nonrepeatable read
    * A transaction re-reads data it has previously read and finds that data has been modified by another transaction (that committed since the initial read).
* phantom read
    * A transaction re-executes a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction
* serialization anomaly
    * The result of successfully committing a group of transactions is inconsistent with all possible orderings of running those transactions one at a time.
* SQL standard isolation levels

|Isolation Level|Dirty Read|Nonrepeatable Read|Phantom Read|Serialization Anomaly|
|---------------|----------|------------------|------------|---------|
|Read uncommitted|Allowed, but not in PG|Possible|Possible|Possible|
|Read committed^|Not possible|Possible|Possible|Possible|
|Repeatable read|Not possible|Not possible|Allowed, but not in PG|Possible
|Serializable|Not possible|Not possible|Not possible|Not possible|

^default in PG

#### Durability

* permanent storage
* committed transactions guaranteed to be on disk
* Write-Ahead Logging (WAL)
    1. Changes are first written to a log
    2. The log is flushed to disk
    3. Only then is the transaction considered committed
* performance cost
    * relax durability for speed
    * `synchronous_commit = off` writes not on disk can be lost on crash

### SQL

* primary keys (PK): `id SERIAL PRIMARY KEY`
* foreign keys (FK): `user_id INTEGER REFERENCES users(id)`
* relationships
    * One-to-One: a user and their profile settings
    * One-to-Many: users and posts (one user can have many posts)
    * Many-to-Many: users and the posts they like
        * use junction/associative tables to connect 2 tables together
        ```sql
        CREATE TABLE chatgroup_participant (
        chatgroup_id INT,
        user_id INT,

        -- dedicate 'id' as PK is not required
        PRIMARY KEY (chatgroup_id, user_id),
        FOREIGN KEY (chatgroup_id) REFERENCES chatgroups(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
        );
        ```
* normalization
    * avoid duplicating data
    * maintain data integrity
    * make data model flexible
    * denormalize for performance (to avoid joins)
* `JOIN`
#TODO: add

#### Commands

1. DDL (Data Definition Language)
    * Creates and modifies database structure
    * Examples: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`
2. DML (Data Manipulation Language)
    * Manages data within tables
    * Examples: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
3. DCL (Data Control Language)
    * Controls access permissions
    * Examples: `GRANT`, `REVOKE`
4. TCL (Transaction Control Language)
    * Manages transactions
    * Examples: `BEGIN`, `COMMIT`, `ROLLBACK`

### Caching

#### Goals

* Save aggregated metrics
* Reduce # of db queries
* Speed up expensive queries

#### Eviction Policies

* **Least Recently Used (LRU)**: Evicts the least recently accessed items first.
* **First In, First Out (FIFO)**: Evicts items in the order they were added.
* **Least Frequently Used (LFU)**: Removes items that are least frequently accessed.

#### Cache Invalidation Strategies

#TODO: cleanup

* **Time-based expiration (TTL)** - Set a fixed lifetime for cached entries. Simple to implement but means serving potentially stale data until expiration.
* **Write-through invalidation** - Update or delete cache entries immediately when writing to the database. Ensures consistency but adds latency to write operations and requires careful error handling.
* **Write-behind invalidation** - Queue invalidation events to process asynchronously. Reduces write latency but introduces a window where stale data might be served.
* **Tagged invalidation** - Associate cache entries with tags (e.g., `user:123:posts`). Invalidate all entries with a specific tag when related data changes. Powerful for complex dependencies but requires maintaining tag relationships.
* **Versioned keys** - Include version numbers in cache keys. Increment the version on updates, naturally invalidating old cache entries. Simple and reliable but requires version tracking.

#### Cache Write Strategies

#TODO: cleanup

* **Write-Through Cache**: Writes data to both the cache and the underlying datastore simultaneously. Ensures consistency but can be slower for write operations.
* **Write-Around Cache**: Writes data directly to the datastore, bypassing the cache. This can minimize cache pollution but might increase data fetch times on subsequent reads.
* **Write-Back Cache**: Writes data to the cache and then asynchronously writes the data to the datastore. This can be faster for write operations but can lead to data loss if the cache fails before the data is written to the datastore.

#### Hot Keys

* distribute load across multiple nodes
* reading hot keys
    * create multiple copies w/ different suffixes stored on different nodes
        * `user:123#1` on node A
        * `user:123#2` on node B
        * `user:123#3` on node C
    * reads: randomly choose one of suffixed keys
    * writes: update all keys to maintain consistency
* writing hot keys
    * write batching: buffer writes every 50-100ms
    * sharding hot keys w/ suffixes
        * split values across shards
        * reading requires summing across shards

#### High-Performant Caches

* data structs
    * A hash table for storing our key-value pairs
    * A linked list for our LRU eviction policy

1. Asynchronous replication for high availability and handling hot key reads.
2. Consistent hashing for sharding and routing.
3. Random suffixes for distributing hot key writes across nodes.
4. Write batching and connection pooling for decreasing network latency/overhead.

### Database Indexes

#### B-Tree Indexes

* the default choice
* benefits
    * maintain sorted order, making range queries & `ORDER BY` operations efficient
    * self-balancing, ensuring predictable performance even as data grows
    * minimize disk I/O by matching their structure to how databases store data
    * handle both equality searches (`email = 'x'`) and range searches (`age > 25`) equally well
    * remain balanced even with random inserts and deletes, avoiding the performance cliffs you might see with simpler tree structures
* real-world examples
    * PostgresSQL
    * DynamoDB
    * MongoDB

#### LSM Trees

* Log-Structured Merge Trees
* for write-heavy loads
    * time-series dbs
    * logging sys
    * analytics platforms
* convert many small random writes into fewer large sequential writes, increasing efficiency
* on write
    * **Memtable (Memory Component)**: New writes go into an in-memory structure called a memtable, typically implemented as a sorted data structure like a red-black tree or skip list. This is extremely fast since it's all in RAM.
    * **Write-Ahead Log (WAL)**: To ensure durability, every write is also appended to a write-ahead log on disk. This is a sequential append operation, which is much faster than random writes.
    * **Flush to SSTable**: Once the memtable reaches a certain size (often a few megabytes), it's frozen and flushed to disk as an immutable Sorted String Table (SSTable). This is a single sequential write operation that can write megabytes of data at once.
    * **Compaction**: Over time, you accumulate many SSTables on disk. A background process called compaction periodically merges these files, removing duplicates and deleted entries. This keeps the number of files manageable and maintains read performance.
* on read
    * Bloom Filters
    * Sparse Indexes
    * Compaction Strategies
* real-world examples
    * Cassandra
    * RocksDB
    * DynamoDB

#### Hash Indexes

* for exact match queries
* persistent hash maps, `O(1)` lookups
* useless for range queries or sorting
* real-world examples
    * Redis

#### Geospatial Indexes

* Geohash: Redis
    * B-Tree indexes treat latitude & longitude as independent dimensions
    * converts a 2D location into a 1D string
    * not density-dependent: everything is split in 4s
    * great for high freq of writes
    * locations close to each other have same prefix (i.e. preserve proximity)
    * use a B-Tree index to handle spatial queries for matching prefixes
* QuadTree
    * not as common as other 2
    * uses recursive spatial subdivision
    * good for uneven densities & low freq of updates
    * key insight
        * dense areas get subdivided more finely
        * sparse regions maintain large quadrants
    * disadvantage: require specialized tree structures
* R-Tree
    * default spatial indexing in PostgresSQL and MySQL
    * more flexible & accurate grouping of nearby objects using overlapping rectangles
    * can handle both points & larger shapes in same index struct

#### Inverted Indexes

* for advanced text search
* word to docs lists
* real-world examples
    * ElasticSearch
    * PG's GIN

#### Index Optimizations

* Composite Indexes
    * multi-column indexes
    * order matters: order columns from most selective to least selective
* Covering Indexes
    * all columns needed by query

## Patterns

### Scaling Reads

1. Optimize read performance within your database
    * [indexing](#database-indexes)
        * prevent DBs from doing full table scans for `WHERE` clauses
        * under-indexing kills more applications than over-indexing ever will
    * [*modern* hardware](#modern-hardware-limits) upgrades
    * denormalization strategies
        * consider read/write ratio
        * use materialized views to precompute expensive aggregations
        ```sql
        -- Instead of this expensive query on every page load:
        SELECT p.*, AVG(r.rating) as avg_rating 
        FROM products p 
        JOIN reviews r ON p.id = r.product_id 
        GROUP BY p.id;

        -- Precompute and store the average:
        CREATE MATERIALIZED VIEW product_ratings AS
        SELECT p.*, AVG(r.rating) as avg_rating
        FROM products p 
        JOIN reviews r ON p.id = r.product_id 
        GROUP BY p.id;
        ```
2. Scale your database horizontally
    * read replicas
        * consider replication lag
        * leader-follower replication
            * write to leader/primary
            * read from replicas
        * *synchronous* replication ensures data consistency but introduces latency
        * *asynchronous* replication is faster but introduces potential data inconsistencies
    * DB sharding
        * smaller DBs, faster queries: distribute load across multiple DBs
        * functional sharding (federation?)
            * `user` data in one DB
            * `product` data in another
3. Add external [caching](#caching) layers
    * application-level caching
    * CDN and edge caching

### Scaling Writes

Key insight: goal is to **reduce throughput per component**.

1. Vertical Scaling and Database Choices
    * consider [*modern* hardware limits](#modern-hardware-limits)
    * DB choices
        * Time-series databases: InfluxDB, TimescaleDB
        * Log-structured databases: LevelDB
        * Column stores: ClickHouse
    * optimize for *writes*
        * disable expensive features: foreign key constraints, expensive triggers
        * tune write-ahead logging: batch transactions
        * reduce index overhead: fewer indexes, faster writes
2. Sharding and Partitioning
    * sharding ~ partitioning
        * sharding: splitting data across multiple machines/nodes
        * partitioning: splitting data within a single db/sys
    * horizontal sharding (partitioning): split *rows*
        * select a good partitioning key
            * `userId` vs `country`
            * minimize variance in # of writes/shard
        * rows for the same `userId` written to same shard
        * slot numbers: Redis
        * consistent hasing: Cassandra, DynamoDB
    * vertical partitioning: split *columns*/tables
        * split tables (e.g. `post`) by reads/writes
        * core `post_content`: write-once, read-many
        * engagement `post_metrics`: high-frequency writes
        * `post_analytics` data: append-only, time-series
3. Handling Bursts with Queues and Load Shedding
    * write queues for burst handling: burst absorption
    * load shedding strategies
        * drop overwritables writes
        * example: location updates in Uber
4. Batching and Hierarchical Aggregation

## Key Technologies

### Redis

* a "data structure store" written in C
* mode
    * single-node
    * replicated: for HA
    * cluster
        * client uses hash slots to map keys to nodes
        * nodes use gossip protocol to redirect to correct node
* scale by structuring keys

#### Data Structures

* Strings
* Hashes (Objects)
* Lists
* Sets
* Sorted Sets (Priority Queues)
* Bloom Filters
* Geospatial Indexes
* Time Series

#### Cache

#TODO: add

#### Distributed Lock

* single instance, no replicas to avoid race conditions
* simple lock using `INCR`
    * acquire a lock using `INCR` w/ TTL
    * if response is 1, we own it
    * else, not ours, retry
    * `DEL` when done
* simple lock using `SET`
    * acquire lock by setting a specific key to random value w/ TTL
    ```
    SET resource_name my_random_value NX PX 30000
    ```
    * release lock: only if key exists and value matches
    ```lua
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end
    ```
    * avoids removing a lock created by another client
* race condition if replicas
    1. Client A acquires the lock in the master.
    2. The master crashes before the write to the key is transmitted to the replica.
    3. The replica gets promoted to master.
    4. Client B acquires the lock to the same resource A already holds a lock for. SAFETY VIOLATION!

#### Leaderboard

* sorted sets
* `log(n)` run-time
* high throughput, low latency

#### Rate Limiting

* fixed-window rate limiter: guarantee reqs < `N` over fixed window `W`

#### Proximity Search

* geospatial indexes using `GEOADD` and `GEOSEARCH`
* runs in `O(N+log(M))` time
    * `N`: the number of elements in the radius
    * `M`: the number of items inside the shape
* Geohashing >> PostGIS

#### Event Sourcing

* streams: append-only logs similar to Kafka's topics
* durably add items to a log
* distributed mechanism for consuming items from the logs
* use cases
    * worker queues

#### Pub/Sub

* broadcast msgs to multiple subscribers in real-time
```
SPUBLISH channel message   # Sends a message to all subscribers of 'channel' (the S prefix means "sharded")
SSUBSCRIBE channel         # Listens for messages on 'channel'
```
* use cases
    * chat systems
    * real-time notifications
* sharding is supported in newer versions
* 1 connection per node, not per channel: `connections == nodes`!
* no persistence!

#### Limitations

* see [hot key](#hot-keys) issues

### Kafka

A distributed commit log

#### Terms

* brokers
    * physical/virtual servers
    * a Kafka cluster consistes of brokers
* partition
    * a *physical* grouping of messages
    * a way to scale data
    * *immutable* seq of msgs, many per broker
    * an append-only log file
* topic
    * a *logical* grouping of partitions/messages
    * a way to organize data
    * multi-producer: 0, 1, many per topic
    * publishing/consuming mgs to/from topics
* producer
* consumer
    * pull-based model
    * organized in consumer groups
* consumer group
    * ensure messages consumed by *exactly one* consumer in group
* message: record
    * headers
    * key: optional (determines partition assignment)
    * value
    * timestamp

#### Design & Processes

* publishing a message
    * partition determination
        * hash msg key to partition
        * if no key, round-robin
        * ensures msgs w/ same key assigned to same paritition
    * broker assignment
        * given partition, get me broker
        * determined by Kafka controller
        * producer sends directly to broker
* append-only design benefits
    * immutability: simplifies replication/recovery/consistency
    * efficiency: minimizes disk seek times
    * scalability: horizontal scaling by increasing partitions & brokers
* replication: leader-follower model
    * leader replication assignment
        * assigned to a broker
        * responsible for all reads/writes for partition
    * follower replication
        * multiple replicas across brokers
        * do not handle clients requests
        * passively replicate data
        * act as backups
    * synchronization & consistency
        * continuous sync of followers w/ leader replica
        * auto-promotion of follower replica to leader
    * controller's role
        * manages replication process
        * monitors health of brokers
        * manages leadership & replication
* pull-based model
    * lets consumers control consumption rate
    * simplifies error handling
    * prevents overwhelming slow consumers
    * enables efficient batching

#### Use Cases

* as message queue: consumers ack
    * asynchronous processing: uploading large files (but not on Kafka! queue events for processing them)
    * in order message processing: waiting queues
    * decouple producer from consumer to scale independently
* as stream: consumers don't ack
    * real-time flow: continuous & immediate process of incoming data
    * simultaneous processing by multiple consumers: pub/sub system

#### Scalability

* numbers
    * small messages: up to 1MB
    * store up to 1TB per broker
    * up to 1M msgs/s per broker
    * 50KB per topic: cap on max topics
* horizontal scaling w/ more brokers
    * add more brokers to cluster
    * need sufficient partitions/topic to use additional brokers
    * more paritions, better load distribution through parallelism
* paritition strategy: main focus
    * `partition = hash(key) % num_partitions`
    * `hash()` is murmur2
    * evenly distribute keys across paritions
    * scaling topics based on throughput
        * high: many partitions
        * low: single partition
* handling hot partitions
    * random paritioning w/o key
        * even distribution
        * but lose order guarantee
    * random salting
        * adding random number/timestamp to key
        * helps distribute load across partitions
        * complicates aggregation logic on consumer side
    * use a compound key
        * combine multiple attributes into a key: `adId`, `userId`
        * better if both attributes vary independently
    * back pressure
        * slow down producer by making it check the lag

#### Fault Tolerance & Durability

* max durability: `acks=all`, msg acked only when all replicas recv-ed it
* replication factor: 3 by default (2 replicas/partition)
* "always available, sometimes consistent"
* Kafka going down: not very realistic!
* consumer goes down
    * offset management
        * offset committed by consumer after processing msg
        * read last committed offset on consumer restart/after crash
    * rebalancing
        * consumer goes down, redistribute partitions across remaining consumers
* commit offset *after* work is done
* keep the consumer work as small as possible

#### Handling Retries & Errors

* producer retries: automatic, but set `idempotent` to true
* consumer retries: not supported, but can be implemented using retry & DLQ topics

#### Performance Optimizations

* batch msgs in producer
    * increase `batch.size`
    * increase `linger.ms` (wait) time for broker (default is 0)
* compress msgs in producer
* maximize parallelism by ensuring msgs evently distributed across partitions

#### Retention Policies

* default: 7 days (168h)
* `retention.ms`
* `retention.bytes`: -1 (no size limit)

### PostgresSQL

#### Reads: Basic Indexing

* B-tree indexes use cases
    * exact matching: `WHERE email = 'user@example.com'`
    * range queries: `WHERE created_at > '2024-01-01'`
    * sorting: `ORDER BY` username if the `ORDER BY` column match the index columns' order
* indexing cost
    * make writes slower (index updates)
    * take up space
    * may be unused if planner chooses sequential scanning
* example
```sql
-- This is your bread and butter index
CREATE INDEX idx_users_email ON users(email);

-- Multi-column indexes for common query patterns
CREATE INDEX idx_posts_user_date ON posts(user_id, created_at);
```

#### Reads: Beyond Basic Indexes

* **GIN (Generalized Inverted Indexes)**: full-text search
```sql
-- Add a tsvector column for search
ALTER TABLE posts ADD COLUMN search_vector tsvector;
CREATE INDEX idx_posts_search ON posts USING GIN(search_vector);

-- Now you can do full-text search
SELECT * FROM posts 
WHERE search_vector @@ to_tsquery('postgresql & database');
```
* GIN features
    * Word stemming (finding/find/finds all match)
    * Relevance ranking
    * Multiple languages
    * Complex queries with AND/OR/NOT
* consider ElasticSearch instead for
    * More sophisticated relevancy scoring
    * Faceted search capabilities
    * Fuzzy matching and "search as you type" features
    * Distributed search across very large datasets
    * Advanced analytics and aggregations
* **JSONB columns with GIN indexes**: store metadata on posts
```sql
-- Add a JSONB column for post metadata
ALTER TABLE posts ADD COLUMN metadata JSONB;
CREATE INDEX idx_posts_metadata ON posts USING GIN(metadata);

-- Now we can efficiently query posts with specific metadata
SELECT * FROM posts 
WHERE metadata @> '{"type": "video"}' 
  AND metadata @> '{"hashtags": ["coding"]}';

-- Or find all posts that mention a specific user
SELECT * FROM posts 
WHERE metadata @> '{"mentions": ["user123"]}';
```
* **Geospatial Search with PostGIS**: index location data for efficient geospatial queries implemented as R-tree 
```sql
-- Enable PostGIS
CREATE EXTENSION postgis;

-- Add a location column to posts
ALTER TABLE posts 
ADD COLUMN location geometry(Point);

-- Create a spatial index
CREATE INDEX idx_posts_location 
ON posts USING GIST(location);

-- Find all posts within 5km of a user
SELECT * FROM posts 
WHERE ST_DWithin(
    location::geography,
    ST_MakePoint(-122.4194, 37.7749)::geography, -- SF coordinates
    5000  -- 5km in meters
);
```
* PostGIS features
    * Different types of spatial data (points, lines, polygons)
    * Various distance calculations (as-the-crow-flies, driving distance)
    * Spatial operations (intersections, containment)
    * Different coordinate systems
    * uses GIST (Generalized Search Tree) implemented as R-trees
* GIN + PostGIS example
```sql
SELECT * FROM posts 
WHERE search_vector @@ to_tsquery('food')
  AND metadata @> '{"type": "video", "hashtags": ["restaurant"]}'
  AND ST_DWithin(
    location::geography,
    ST_MakePoint(-122.4194, 37.7749)::geography,
    5000
  );
```
* `UNIQUE` constraint on 2 columns
```sql
ALTER TABLE reviews
ADD CONSTRAINT unique_user_business UNIQUE (user_id, business_id);
```

#### Reads: Query Optimization Essentials

* covering indexes
    * store all data (`SELECT` columns) in index
    * pros: satisfy entire query from index w/o reading table
    * cons: bigger indexes & slower writes
    * example
    ```sql
    -- Let's say this is a common query in our social media app:
    SELECT title, created_at 
    FROM posts 
    WHERE user_id = 123 
    ORDER BY created_at DESC;

    -- A covering index that includes all needed columns
    CREATE INDEX idx_posts_user_include 
    ON posts(user_id) INCLUDE (title, created_at);
    ```
* partial indexes
    * index a subset of data (e.g. active users only)
    * example
    ```sql
    -- Standard index indexes everything
    CREATE INDEX idx_users_email ON users(email);  -- Indexes ALL users

    -- Partial index only indexes active users
    CREATE INDEX idx_active_users 
    ON users(email) WHERE status = 'active';  -- Smaller, faster index
    ```

#### Reads: Practical Performance Limits

1. Query Performance
    * Simple indexed lookups: tens of thousands per second per core
    * Complex joins: thousands per second
    * Full-table scans: depends heavily on whether data fits in memory
2. Scale Limits
    * Tables start getting unwieldy past 100M rows
    * Full-text search works well up to tens of millions of documents
    * Complex joins become challenging with tables >10M rows
    * Performance drops significantly when working set exceeds available RAM

#### Writes: Steps

1. **Transaction Log (WAL) Write** [Disk]
    * changes are first written to the WAL on disk
    * a sequential write operation, making it relatively fast
    * the WAL is critical for durability
    * once changes are written here, the transaction is considered durable because even if the server crashes
2. **Buffer Cache Update** [Memory]
    * changes are made to the data pages in PostgreSQL's shared buffer cache, where the actual tables and indexes live in memory
    * when pages are modified, they're marked as "dirty" to indicate they need to be written to disk eventually
3. **Background Writer** [Memory → Disk]
    * dirty pages in memory are periodically written to the actual data files on disk
    * happens *asynchronously* through the background writer, when memory pressure gets too high, or when a checkpoint occurs
    * delayed write strategy allows PostgreSQL to batch multiple changes together for better performance
4. **Index Updates** [Memory & Disk]
    * Each index needs to be updated to reflect the changes
    * Like table data, index changes also go through the WAL for durability
    * This is why having many indexes can significantly slow down writes - each index requires additional WAL entries and memory updates.
* write performance bounded by
    * how fast you can write to the WAL (disk I/O)
    * how many indexes need to be updated
    * how much memory is available for the buffer cache

####  Writes: Throughput Limitations

Assuming PostgreSQL's *default* transaction isolation level (**Read Committed**: preventing dirty reads)

* single instance on *good* hardware
    * Simple inserts: ~5,000/s per core
    * Updates with index modifications: ~1,000-2,000/s per core
    * Complex transactions (multiple tables/indexes): Hundreds per second
    * Bulk operations: Tens of thousands of rows per second
* factors
    * Hardware: Write throughput is often bottlenecked by disk I/O for the WAL
    * Indexes: Each additional index reduces write throughput
    * Replication: If configured, synchronous replication adds latency as we wait for replicas to confirm
    * Transaction Complexity: More tables or indexes touched = slower transactions

#### Writes: Optimizations

1. Vertical Scaling: faster machines
2. Batch Processing: batch writes together
3. Write Offloading: write async using queues
4. Table Partitioning
    * most common: time-based
    * split by multiple physical tables
5. (Horizontal) Sharding
    * common: by `user_id`
    * rows for same `user_id` written to same shard
    * adds complexity
        * need to handle cross-shard queries
        * maintain consistent schemas across shards
        * manage multiple dbs
    * no native PostgresSQL support

#### Replication

* purpose
    * scaling reads by distributing queries across replicas
    * providing high availability in case of node failures
* synchronous: stronger consistency, higher latency
* asynchronous: better performance, potential inconsistencies b/w replicas
* hybrid approach
    * small number of sync replicas for consistency
    * more async replicas for read scaling
* scaling reads
    * distribute read queries across multiple dbs
    * send writes to primary
    * replication lag: "read-your-writes" consistency
* high availability: promote replicas to become primaries if primary fails

#### Transactions

* a set of ops to execute together
* must all succeed or fail
* simple transaction: ensures atomicity
```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```
* transactions by themselves don't guarantee consistency
* concurrent transactions: consistency problem!
```sql
BEGIN;
-- Get current max bid for item 123
SELECT maxBid from Auction where id = 123;

-- Place new bid if it's higher:
-- if 2 bids get inserted at the same time based on value of maxBid
-- the committed bid may not be the highest!
INSERT INTO bids (item_id, user_id, amount) 
VALUES (123, 456, 100);

-- Update the max bid
UPDATE Auction SET maxBid = 100 WHERE id = 123;
COMMIT;
```
* solving concurrency issues
    * row-level locking
        * lock rows you are reading
        * by using `FOR UPDATE` at end of `SELECT` *inside* transaction
        * preferred when you know which row to lock
    * higher isolation level
        * stricter isolation levels
        ```sql
        BEGIN;
        SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

        -- Same code as before...

        COMMIT;
        ```
        * conflicting transactions get rolled back
        * requires app-level retry
        * for complex transactions
* consistency guarantees
    * **Read Committed** (Default)
        * default isolation level
        * only sees data that was committed before the query began
    * **Repeatable Read**
        * provides stronger guarantees than the SQL standard requires
        * creates a consistent snapshot of the data as of the start of the transaction
        * prevents non-repeatables reads AND phantom reads
    * **Serializable**
        * strongest isolation level
        * makes transactions behave as if they were executed one after another in sequence

|Aspect|Serializable Isolation|Row-Level Locking|
|------|----------------------|-----------------|
|Concurrency|Lower - transactions might need to retry on conflict|Higher - only conflicts when touching same rows|
|Performance|More overhead - must track all read/write dependencies|	Less overhead - only locks specific rows
|Use Case|Complex transactions where it's hard to know what to lock|When you know exactly which rows need atomic updates
|Complexity|Simple to implement but requires retry logic|More explicit in code but no retries needed
|Error Handling|Must handle serialization failures|Must handle deadlock scenarios
|Example|Complex financial calculations across multiple tables|Auction bidding, inventory updates
|Memory Usage|Higher - tracks entire transaction history|Lower - only tracks locks
|Scalability|Doesn't scale as well with concurrent transactions|Scales better when conflicts are rare

#### Use Cases

Default DB choice because:
1. Provides strong ACID guarantees while still scaling effectively with replication and partitioning
2. Handles both structured and unstructured data through JSONB support
3. Includes built-in solutions for common needs like full-text search and geospatial queries
4. Can scale reads effectively through replication
5. Offers excellent tooling and a mature ecosystem
6. Complex relationships between data

Alternatives for:
1. **Extreme Write Throughput**: in PG, each write requires WAL entry and index update
    * NoSQL databases (like Cassandra) for event streaming
    * Key-value stores (like Redis) for real-time counters
2. **Global Multi-Region Requirements**: in PG, single-primary arch, 1 primary writer
    * CockroachDB for global ACID compliance
    * Cassandra for eventual consistency at global scale
    * DynamoDB for managed global tables
3. **Simple Key-Value Access Patterns**: PG is overkill! 
    * Redis for in-memory performance
    * DynamoDB for managed scalability
    * Cassandra for write-heavy workloads

## LeetCode Design Template

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

* Product Design Questions
```
Requirements -> Core Entities -> API -> High-Level Design -> Deep Dive
```
* Infrastructure Design Questions
```
Requirements -> System Interface & Data Flow -> High-Level Design -> Deep Dive
```
* overcommunicate!
    * explain what you are doing
    * and what you are NOT doing
    * and why

### Requirements
[5 min]

1. Functional: *features* of system
    * core: limit to 3 or so
    * out of scope
2. Non-functional: *qualities* of system
    * core: very important, needed for deep dives
    * out of scope: check in to get feedback on scope
3. Capacity estimations [can skip for later]
    * ask to come back to it during high-level design
    * if the result will have a direct influence on design

### Core Entities
[2 min]

* required for Product Design Qs
* optional for Infrastructure Design Qs
* data model
* tables in storage
* define/document tables next to high-level design for easier updates

### API or System Interface
[5 min]

* API for Product Design
    * schema of API calls
* System Interface for Infrastructure Design
    * Inputs to system
    * Outputs to system
* mistakes
    * spending too much time
    * getting bogged down in details
    * specifying types for each req/resp input/output
    * putting user ids in the req body: instead read from req headers
* 1-1 mapping b/w functional requirements & API
* go over each functional requirement and define an API call
* use core entities to satisfy functional requirements

### Data Flow
[5 min]

* optional for Product Design Qs
* required for Infrastructure Design Qs
* should satisfy functional requirements
* do for Web Crawler & data pipelineing: helps with high-level design

### High-Level Design
[10-15min]

* satisfy functional requirements
* go over each API call and build the high-level design
* use ... for non-important details (e.g. user metadata)
* split into microservices to
    * scale independently
    * satisfy different non-functional reqs: C or A
    * maintain/own by different teams
* don't leave in design obviously non-scalable components

### Deep Dive
[10 min]

* satisfy non-functional requirements
* go over at least 3 areas
* do estimates here (unless you had to in high-level already)
* talk about scalability last so you don't optimize a solution that changes

## System Requirements

* functional
    * define *behavior*: what a system is supposed to do
    * example: exchange messages
    * *who* is going to use the system?
    * *how* are they going to use it?
* non-functional
    * define *qualities*: how a system is supposed to behave
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

```
Power of 1000	Number          Prefix
(1000^x)
----------------------------------------
0	            Unit	
1	            Thousand        Kilo
2	            Million         Mega
3	            Billion         Giga
4	            Trillion        Tera
5	            Quadrillion     Peta
```

### Time

* `86,400 s/day ~ 10^5 s`
* 1 million reqs/s: `10^6 reqs/s / 10^5 s ~ 10 reqs/s` (= 12 reqs/s)
* 2.5 million secs/month
* 1 reqs/second = 2.5 million req/month
* 40 reqs/second = 100 million reqs/month
* 400 reqs/second = 1 billion reqs/month

### Modern Hardware Limits
[as of 2025]

* Single databases can handle terabytes of data
* Caches can hold entire datasets in memory
* Message queues are fast enough for synchronous flows (as long as there is no backlog!)
* Application servers have enough memory for significant local optimization
* 1st bottleneck: CPU utilization, not memory capacity (CPU > memory > network)
* network latency in same cloud region: 1-2ms

|Component|Key Metrics|Scale Triggers|
|---------|-----------|--------------|
|Caching|~1ms latency|Hit rate < 80%|
||100k+ operations/second|Latency > 1ms|
||Memory-bound (up to 1TB)|Memory usage > 80%|
|||Cache churn/thrashing|
|Databases|Up to 50k TPS|Write throughput > 10k TPS|
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
A two-hour movie            1gb
A small book of plain text  1mb
A high-resolution photo	    1mb
A medium-resolution image
(or a site layout graphic)  100kb
```

### Latencies

* Human's perception of real-time: 200ms
* Access times
    * Memory: ~100 nanoseconds (0.0001 ms)
        * 1000x faster than SSD
        * 100,000x faster than HDD
    * SSD: ~0.1 milliseconds
    * HDD: ~10 milliseconds
* IOPS
    * Memory: millions of reads per second
    * SSD: ~100,000 IOPS
    * HDD: ~100-200 IOPS

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

* If queue is unbounded, latency increases. To set max response time, limit queue length
```
max latency = (transaction time / number of threads) * queue length
queue length = max latency / (transaction time / number of threads)
```

### Terminology

* CPS: Clicks Per Second
* CRUD: Create, Read, Update, Delete
* DAU: Daily Active Users
* DLQ: Dead Letter Queues
* IOPS: I/O Per Second
* linearizability: all nodes reflect the most recent write operation
* QPS: Queries Per Second
* scalable: a system is scalable in the range where the cost of adding incremental work is approximately constant
* SSE: Server-Sent Events
* TPS: Transactions Per Second
* WPS: Writes Per Second

### HTTP Codes

* client errors: `4xx`
* server errors: `5xx`
* `200`: OK
* `201`: created resource
* `301`: permanent redirect
* `302`: temporary redirect
* `400`: bad request
* `401`: authentication required
* `404`: not found
* `429`: too many requests
* `500`: server error