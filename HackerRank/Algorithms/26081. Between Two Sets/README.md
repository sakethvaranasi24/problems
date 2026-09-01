# Between Two Sets

> Algorithms | Implementation | HackerRank

## Problem Overview

- Platform: HackerRank
- Domain: Algorithms
- Track: Implementation
- Difficulty: Easy
- Problem ID: 26081
- Max Score: 10
- Problem Link: [https://www.hackerrank.com/challenges/between-two-sets/problem](https://www.hackerrank.com/challenges/between-two-sets/problem)

## Problem

There will be two arrays of integers.  Determine all integers that satisfy the following two conditions:  

1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array

These numbers are referred to as being *between* the two arrays.  Determine how many such numbers exist.

**Example**  
$a = [2, 6]$  
$b = [24, 36]$  

There are two numbers between the arrays: $6$ and $12$.  
$6\%2 = 0$, $6\%6 = 0$, $24\%6 = 0$ and $36\%6 = 0$ for the first value.   
$12\%2 = 0$, $12\%6 = 0$ and $24\%12 = 0$, $36\%12 = 0$ for the second value.
Return $2$.

**Function Description**  

Complete the *getTotalX* function in the editor below.  It should return the number of integers that are betwen the sets.  

getTotalX has the following parameter(s):  

- *int a[n]*: an array of integers  
- *int b[m]*: an array of integers  

**Returns**  

- *int:* the number of integers that are between the sets

## Submission

| Item | Value |
| --- | --- |
| Status | Accepted |
| Language | python3 |
| Score | 10.0 |
| Testcases | 9/9 passed |
| Submission ID | 481762186 |

---

_Synced with AlgorithmHub_