# System Design Questions

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Design URL Shortener](#design-url-shortener)
  - [System Qualities](#system-qualities)
  - [Components & Tech. Stack](#components--tech-stack)
  - [Deep Dives](#deep-dives)
- [Design Dropbox](#design-dropbox)
  - [System Qualities](#system-qualities-1)
  - [Components & Tech. Stack](#components--tech-stack-1)
  - [Deep Dives](#deep-dives-1)
- [Design Ticketmaster](#design-ticketmaster)
- [Design Facebook's News Feed](#design-facebooks-news-feed)
- [Design WhatsApp](#design-whatsapp)
- [Design LeetCode](#design-leetcode)
- [Design Uber](#design-uber)
  - [System Qualities](#system-qualities-2)
  - [Components & Tech. Stack](#components--tech-stack-2)
  - [Deep Dives](#deep-dives-2)
- [Design Web Crawler](#design-web-crawler)
  - [System Qualities](#system-qualities-3)
  - [Components & Tech. Stack](#components--tech-stack-3)
  - [Deep Dives](#deep-dives-3)
- [Design Ad Click Aggregator](#design-ad-click-aggregator)
- [Design Facebook's Post Search](#design-facebooks-post-search)
- [Design a Distributed Cache](#design-a-distributed-cache)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

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
* API Gateway & Load Balancer
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
* [ ] watched

## Design Facebook's News Feed

* [x] read
* [ ] watched

## Design WhatsApp

* [x] read
* [ ] watched

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

* API Gateway & Load Balancer
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