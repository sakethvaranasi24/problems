# Rising Temperature

> Easy | 0197 | LeetCode

## Problem Overview

- Platform: LeetCode
- Difficulty: Easy
- Problem ID: 0197
- Tags: Database
- Problem Link: [https://leetcode.com/problems/rising-temperature/](https://leetcode.com/problems/rising-temperature/)

## Problem

<p>Table: <code>Weather</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
</pre>

<p>&nbsp;</p>

<p>Write a solution to find all dates&#39; <code>id</code> with higher temperatures compared to its previous dates (yesterday).</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
<strong>Output:</strong> 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
<strong>Explanation:</strong> 
In 2015-01-02, the temperature was higher than the previous day (10 -&gt; 25).
In 2015-01-04, the temperature was higher than the previous day (20 -&gt; 30).
</pre>


## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | MySQL |
| Runtime | 466 ms (78.45%) |
| Memory | 0B (100.00%) |
| Submission ID | 2127527823 |

---

_Synced with AlgorithmHub_