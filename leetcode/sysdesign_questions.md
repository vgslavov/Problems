# System Design Questions

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Sources](#sources)
- [Design URL Shortener](#design-url-shortener)
  - [System Qualities](#system-qualities)
  - [Components & Tech. Stack](#components--tech-stack)
  - [Deep Dives](#deep-dives)
- [Design Dropbox](#design-dropbox)
  - [System Qualities](#system-qualities-1)
  - [Components & Tech. Stack](#components--tech-stack-1)
  - [Deep Dives](#deep-dives-1)
- [Design Ticketmaster](#design-ticketmaster)
  - [System Qualities](#system-qualities-2)
  - [Components & Tech. Stack](#components--tech-stack-2)
  - [Deep Dives](#deep-dives-2)
- [Design Facebook's News Feed](#design-facebooks-news-feed)
- [Design WhatsApp](#design-whatsapp)
  - [System Qualities](#system-qualities-3)
  - [Components & Tech. Stack](#components--tech-stack-3)
  - [Deep Dives](#deep-dives-3)
- [Design LeetCode](#design-leetcode)
- [Design Uber](#design-uber)
  - [System Qualities](#system-qualities-4)
  - [Components & Tech. Stack](#components--tech-stack-4)
  - [Deep Dives](#deep-dives-4)
- [Design Web Crawler](#design-web-crawler)
  - [System Qualities](#system-qualities-5)
  - [Components & Tech. Stack](#components--tech-stack-5)
  - [Deep Dives](#deep-dives-5)
- [Design Ad Click Aggregator](#design-ad-click-aggregator)
- [Design Facebook's Post Search](#design-facebooks-post-search)
- [Design a Distributed Cache](#design-a-distributed-cache)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Sources

* [Hello Interview: Question Breakdowns](https://www.hellointerview.com/learn/system-design/problem-breakdowns/overview)
* [LeetCode: System Design Interviews and Beyond: Problems](https://leetcode.com/explore/featured/card/system-design-for-interviews-and-beyond/735/practice-problems/)

## Design URL Shortener

* [x] read
* [x] watched

### System Qualities

1. Uniqueness of short codes
2. Redirection w/ minimal latency (< 100ms)
3. Reliable & available: A >> C
4. Support up to 1B short URLs and 100M DAU

### Components & Tech. Stack

* API Gateway
    * route to microservices
* Write Service
    * get latest count
    * generate short URL
    * save to DB
* Read Service
    * look up long URL in cache/DB
* Global Counter: redis
    * `INCR`
    * single-instance, single-threaded
* Cache: redis
    * read-through
    * LRU eviction
* Database: PG
    * metadata

### Deep Dives

1. Uniqueness of short URLs
    * 6-chars: `62^6`
    * Base62 encoding: `[0-9A-Za-z]`
    * `rand()`: check for collisions
    * hash: `base62(md5(long_url))[:6]`
    * counter: redis `INCR` + Base62 encoding
        * predictable
        * rate limit users
2. Fast redirects
    * use in-memory read-through cache: redis
3. Scaling: supporting 1B URLs & 100M DAU
    * cache lookups: short to long URL
        * `10^8 users/day / 10^5 s/day = 10^3 reqs/s`
        * scale reqs for peak: `10^3 * 10-100 = 10k - 100k reqs/s`
    * URL metadata: `500 bytes * 1B rows = 500GB`
    * counter batching: request batches of counters (1000 at-a-time)

## Design Dropbox

* [x] read
* [x] watched

### System Qualities

1. Highly available: A >> C! (stale files are better than no files)
2. Large files: <= 50GB
3. Secure & reliable, file recovery
4. Low latency: fast upload/download/sync

### Components & Tech. Stack

* Uploader client
    * watch for changes
    * upload directly to S3
* Downloader client 
    * poll for changes
    * sync w/ remote S3 or CDN
* API Gateway & Load Balancer (L7?)
    * routing
    * auth
    * rate limiting
* File Service
    * save metadata to PG
    * get pre-signed URLs from S3
* Blob Storage: S3
    * raw file storage
* Database: PG
    * file metadata
* CDN
    * cache frequently accessed files from S3

### Deep Dives

1. Large files
    * chunking: 5-10MB
    * fingerprinting
        * apply hash: SHA-256
        * fingerprint chunks & entire file
        * maintain status in metadata
    * AWS multi-part uploads API
2. Fast uploads/downloads/sync
    * use compression: consider file type
    * parallelize chunk uploads/downloads
3. File security
    * encryption in transit: HTTPS
    * encryption at rest: S3 encryption
    * access control: ACLs

## Design Ticketmaster

* [x] read
* [x] watched

### System Qualities

1. Availability for searching/viewing events, Consistency for booking events
2. Scalable: high throughput for popular events (10M users per event)
3. Low latency searches (< 500ms)
4. Read heavy: read >> write (100:1)

### Components & Tech. Stack

* API Gateway
    * auth
    * route calls
    * rate limit
* Search Service
    * searching of events
* Event Service
    * viewing of events
* Booking Service
    * reserve: set ticket lock
    * confirm: write to DB ticket booking
    * interact with Payment Processor
* Database: PG
    * store event/ticket/etc. metadata
* Inverted Index DB
    * terms to events index
    * ElasticSearch: PG -CDC-> ElasticSearch
    * PG only: use GIN index
* Distributed Ticket Lock: redis
    * lock tickets for a pre-defined TTL
* Virtual Waiting Queue: redis
    * hold batches of users pre-booking
* Payment Processor: Stripe

### Deep Dives

1. Reserving tickets
    * distributed lock with TTL: redis
    * DB ticket table has only 2 states: available & booked
    * locking entirely in redis
    * challenges
        * single redis node for simple distributed lock
        * no double booking on failure
        * but possibility for bad user experience: error on purchase of already sold tickets due to no reservation
2. Supporting millions of requests for popular events
    * caching: popular events in redis, use TTL
    * load balancing: round robin or least connections across instances
    * horizontal scaling: Events Service is stateless
3. Good user experience for simultaneous bookings
    * virtual waiting queues: redis + WebSockets/SSEs
4. Improve search latencies
    * B-tree indexes are bad for term searches (full table scans)
    * ElasticSearch: feed data from PG over CDC to keep in sync
    * PG+GIN: or use only PG with own Inverted Index
5. Speed up frequently repeated searches
    * good: redis
        * TTLs
        * LRU/LFU
    * great: CDN
        * cache search results
        * client -> CDN -> API Gateway
        * very selective searches will result in cache misses

## Design Facebook's News Feed

* [x] read
* [ ] watched

## Design WhatsApp

* [x] read
* [x] watched

### System Qualities

1. Messages delivered w/ low latency (< 500ms)
2. Guaranteed message delivery
3. High throughput for billions of users
4. Don't unnecessarily store messages (privacy)
5. Fault-tolerant (A > C)

### Components & Tech. Stack

* Client/Device
    * use WebSockets for real-time connectivity
* Load Balancer
    * stateful!
    * route to Chat Server based on least # of connections
    * L4 (due to WebSockets)
* Chat Servers
    * stateful!
    * users connect to any, routed by LB based on load
    * registers a subscription in Redis for userId
    * publish a notification to Redis for the topic on message sent
* Redis Pub/Sub
    * not Kafka!
        * can't scale topics to billions of users
        * topics are too big (50KB)
    * light-weight, near real-time connectivity b/w Chat Servers
        * echoes requests across sockets
    * at most once delivery of messages: no guarantee of delivery
    * however, msgs are persisted to PG and are acked
    * NxM connections (b/w Chat Servers & Redis nodes)
    * uses consistent hashing for adding/removing nodes to Redis cluster
* Database: PG or DynamoDB
    * high throughput & writes
    * store msgs, groups, etc.
        * composite PK on `chatId` & `participantId`
        * look up participants for a chat: range lookup for `chatId`
        * look up chats for a participant: #TODO
    * store undelivered messages in Inbox for retrieval on Client connection
* Blob Storage: S3
    * store attachments
    * client gets pre-signed URLs
    * embeds URLs in msgs
    * interacts w/ S3 directly for to upload/download
* Cleanup Service
    * query DB to delete old & delivered msgs

### Deep Dives

1. Handling billions of users
    * good: consistent hashing of chat servers
        * chat registry to look up chat server to connect to
        * Zookeeper to coordinate
    * great: redis pub/sub #TODO
        * lightweight hash map of socket connections 
        * on connection
            * chat servers subscribe users to topics based on `userId`
            * messages recved on sub, fwd-ed to websocket for that user
        * on msg
            * publish msg to topic for `userId`
            * msg recved by all subscribing Chat Servers
            * Chat Servers fwd msg to user's websocket
    * BOTE
        * msgs/day: `1B users x 100 msgs/day = 100B msgs/day`
        * storage: `1 KB/msg x 100B msgs/day = 100B KB = 100 TB`
2. Handling multiple clients/devices per user
    * map `userId` to `clientId`
    * store `clientId` in msg/chat/inbox tables

## Design LeetCode

* [x] read
* [ ] watched

## Design Uber

* [ ] read
* [x] watched

### System Qualities

1. Low latency matching (< 1 min or fail)
2. Strong consistency in ride matching (1 rider per driver)
3. High throughput during peak times (100k reqs per location)

### Components & Tech. Stack

* API Gateway & Load Balancer (L7?)
    * routing
    * auth
    * rate limiting
* Ride Service
    * fare estimation
    * ride creation
    * trigger matching
    * store drivers' accept/decline
* Match Queue
    * match requests for drivers
* Ride Matching Service
    * match drivers & riders
    * fetch closest drivers
* Location Service
    * updates riders/drivers' locations
* Location DB: redis
    * store drivers' current location
* 3rd party Mapping service
    * provide map data
* Database: PG
    * store riders & drivers metadata
    * store ride & estimates
* Distributed Lock: redis
    * check driver's outstanding ride req
* Ride Client
* Driver Client
* Notification Service: iOS or Android

### Deep Dives

1. Frequent driver location updates & efficient proximity location searches
    * high freq of writes: DynamoDB or PG
    * location query efficiency
        * good: PG's PostGIS indexes
        * great: redis geohashing
2. Preventing system overload from frequent location updates & ensuring accuracy
    * adaptive location update intervals
    * load shedding: dropping some location updates
        * at peak times
        * when parked
3. Ensuring 1 request per driver
    * distributed lock w/ TTL: redis
    * Ride Matching Service attempt to acquire `driverId` lock
    * if TTL (10s) expires w/o driver accepting, lock is released
    * else, lock set to accepted
4. Processing every ride request during peak times
    * queue w/ dynamic scaling: Kafka or SQS
    * add Matching Queue b/w Ride Service & Ride Matching Service
5. Ensuring drivers respond timely
    * durable execution using Temporal or AWS Step Functions
    * set time outs per driver
    * move on to next driver until accept
6. Scaling: reducing latency & increasing throughput
    * geo-sharding w/ read replicas
        * scale horizontally by sharding by location

## Design Web Crawler

* [ ] read
* [x] watched

### System Qualities

1. Fault tolerance
2. Politeness (respect `robots.txt`)
3. Scale to 10B pages
4. Efficient crawling in 5D

### Components & Tech. Stack

* Frontier Queue: Kafka or SQS
    * seed URLs: bootstrap
    * extracted URLs by parser
* Parsing Queue: Kafka or SQS
    * S3 links for raw HTML to parse
* Crawler
    * query DNS
    * crawl: fetch webpages
    * store webpages to S3
    * queue S3 links to Parsing Queue
* Parsing workers
    * rad S3 links from Parsing Queue
    * get raw HTML from S3
    * parse!
    * store parsed HTML to S3
    * queue extracted URLs to Frontier Queueu
* Blob storage: S3
    * raw HTML
    * parsed HTML
* Database: PG
    * URL metadata
* Rate Limiter & DNS Cache: redis
    * cache domain to IP to minimize DNS lookups
    * rate limit crawling to respect `robots.txt`
* DNS
    * multiple DNS providers

### Deep Dives

1. Fault tolerance & resuming crawling
    * multi-stage pipeline: split crawling & parsing
    * Kafka w/ exponential backoff
        * retry topic
        * DLQ topic
    * don't commit offset to Kafka until saving HTML to S3
2. Ensuring politeness
    * respecting `robots.txt`
        * store crawl delay & disallow in metadata db
    * rate limiting
        * industry standard: 1 request per domain per second
        * global, domain-specific rate limiting
        * sliding window: reqs per domain per s
3. Scaling to 1B pages in 5D
    * network-optimized AWS instances: `400 Gbps`
    * bandwidth: `400 Gbps / 8 bits/byte = 50 MB/s`
    * pages: `50 MB/s / 2 MB/page = 25k pages/s`
    * scaling: `25k pages/s * 30% = 7,500 pages/s`
    * days/node: `10^10 pages / 7,500 pages/s = 1,333,333 s / 10^5 s/day = 15 days`
    * `15 days / 4 nodes ~ 4 days`
    * set max depth or crawling per domain to avoid crawler traps

## Design Ad Click Aggregator

* [ ] read
* [ ] watched

## Design Facebook's Post Search

* [ ] read
* [ ] watched

## Design a Distributed Cache

* [x] read
* [ ] watched