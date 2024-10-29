# SQL 50

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Select](#select)
- [Basic Joins](#basic-joins)
- [Basic Aggregate Functions](#basic-aggregate-functions)
- [Sorting and Grouping](#sorting-and-grouping)
- [Advanced Select and Joins](#advanced-select-and-joins)
- [Subqueries](#subqueries)
- [Advanced String Functions/Regex/Clause](#advanced-string-functionsregexclause)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Select

* 1757: Recyclable and Low Fat Products #easy
```
SELECT product_id
FROM products
WHERE low_fats = "Y" AND recyclable = "Y"
```
* 584: Find Customer Referee #easy
```
SELECT name
FROM customer
WHERE referee_id <> 2 OR referee_id IS NULL
```
* 595: Big Countries #easy
```
SELECT name, population, area
FROM world
WHERE area >= 3000000 OR population >= 25000000
```
* 1148: Article Views I #easy
```
SELECT distinct author_id AS id
FROM views
WHERE author_id = viewer_id
ORDER BY id
```
* 1683: Invalid Tweets #easy
```
SELECT tweet_id
FROM tweets
WHERE LENGTH(content) > 15
```

## Basic Joins

* 1378: Replace Employee ID with the Unique Identifier #easy
```
SELECT unique_id, name
FROM employees
LEFT JOIN employeeuni ON employees.id = employeeuni.id
```
* 1068: Product Sales Analysis I #easy
```
SELECT product_name, year, price
FROM sales
LEFT JOIN product ON product.product_id = sales.product_id
```
* 1581: Customer Who Visited but Did Not Make Any Transactions #easy #mistakes
```
SELECT customer_id, COUNT(*) AS count_no_trans
FROM visits
LEFT JOIN transactions ON visits.visit_id = transactions.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id
```
* 197: Rising Temperature #easy #mistakes
    * `DATEDIFF()`
        ```
        SELECT w1.id
        FROM weather AS w1
        JOIN weather AS w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
        WHERE w1.temperature > w2.temperature
        ```
    * subquery
        ```
        SELECT w1.id
        FROM weather AS w1
        WHERE w1.temperature > (
            SELECT w2.temperature
            FROM weather AS w2
            WHERE w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 DAY)
        );
        ```
    * Cartesian Product (a.k.a. cross join)
        ```
        SELECT w2.id
        FROM weather AS w1, weather as w2
        WHERE DATEDIFF(w2.recordDate, w1.recordDate) = 1
        AND w2.temperature > w1.temperature
        ```
* 1661: Average Time of Process per Machine #easy #mistakes
```
SELECT a.machine_id, ROUND(AVG(b.timestamp-a.timestamp), 3) AS processing_time
FROM activity as a, activity as b
WHERE a.machine_id = b.machine_id
AND a.process_id = b.process_id
AND a.activity_type = "start"
AND b.activity_type = "end"
GROUP BY a.machine_id
```

## Basic Aggregate Functions

## Sorting and Grouping

## Advanced Select and Joins

## Subqueries

## Advanced String Functions/Regex/Clause
