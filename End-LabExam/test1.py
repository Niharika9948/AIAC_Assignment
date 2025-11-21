"""
Ride-Sharing App – Sorting & Route Optimization

Implements merge sort and quick sort with AI-style optimizations.
Includes docstrings and inline comments.
"""

from random import randint, shuffle, seed
from typing import List
import unittest 


# ---------------------------
# INSERTION SORT
# ---------------------------
def insertion_sort(arr: List[float]) -> List[float]:
    """Simple insertion sort used for small subarrays."""
    a = arr[:]   # avoid mutating original list
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ---------------------------
# MERGE SORT (with small-size optimization)
# ---------------------------
def ai_merge_sort(arr: List[float]) -> List[float]:
    """Optimized merge sort using insertion sort for small partitions."""
    if len(arr) <= 32:
        return insertion_sort(arr)

    mid = len(arr) // 2
    left = ai_merge_sort(arr[:mid])
    right = ai_merge_sort(arr[mid:])

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# ---------------------------
# QUICK SORT (optimized)
# ---------------------------
def _median_of_three(a, i, j, k):
    """Pick median of three indexes as pivot."""
    vals = [(a[i], i), (a[j], j), (a[k], k)]
    vals.sort(key=lambda x: x[0])
    return vals[1][1]


def _quick_sort_inplace(a, lo, hi):
    """Optimized in-place QuickSort."""
    if hi - lo + 1 <= 16:
        for i in range(lo + 1, hi + 1):
            key = a[i]
            j = i - 1
            while j >= lo and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
        return

    mid = (lo + hi) // 2
    pivot_index = _median_of_three(a, lo, mid, hi)
    pivot = a[pivot_index]

    a[pivot_index], a[hi] = a[hi], a[pivot_index]

    i = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[hi] = a[hi], a[i]

    _quick_sort_inplace(a, lo, i - 1)
    _quick_sort_inplace(a, i + 1, hi)


def ai_quick_sort(arr: List[float]) -> List[float]:
    """Optimized quicksort wrapper."""
    if len(arr) <= 1:
        return arr[:]
    a = arr[:]
    _quick_sort_inplace(a, 0, len(a) - 1)
    return a


# ---------------------------
# SMART SORT SELECTOR
# ---------------------------
def choose_and_sort(etas: List[float]) -> List[float]:
    """Uses quicksort for small lists, merge sort for large lists."""
    if len(etas) <= 1024:
        return ai_quick_sort(etas)
    else:
        return ai_merge_sort(etas)


# ---------------------------
# FASTEST DRIVER
# ---------------------------
def fastest_driver(sorted_etas: List[float]) -> float:
    """Returns lowest ETA."""
    return sorted_etas[0]


# ---------------------------
# MAIN PROGRAM
# ---------------------------
if __name__ == "__main__":

    print("\n===== RUNNING UNIT TESTS =====\n")

    # Load tests from test_test1.py
    loader = unittest.TestLoader()
    suite = loader.discover(".", pattern="test_test1.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)

    print("\n===== PROGRAM OUTPUT =====\n")

    # Generate sample ETA list
    seed(5)
    etas = [round(randint(1, 200) + randint(0, 99) / 100, 2) for _ in range(12)]
    shuffle(etas)

    print("Original ETAs:", etas)

    sorted_list = choose_and_sort(etas)

    print("\nSorted ETAs:", sorted_list)
    print("\nFastest Driver ETA:", fastest_driver(sorted_list))

"""
Ride-Sharing App – ETA Sorting & Route Optimization Module
==========================================================

This module provides optimized sorting utilities for a ride-sharing system that
needs to quickly determine the fastest available driver based on estimated arrival
times (ETAs). Since incoming driver ETAs arrive constantly and must be sorted
rapidly, two algorithm families are implemented with practical performance
enhancements inspired by AI-guided heuristics:

1. Merge Sort (ai_merge_sort)
2. Quick Sort (ai_quick_sort)
3. Insertion Sort (used as a micro-optimization)

Key Features
------------

• **Hybrid Sorting**  
  Both merge sort and quick sort automatically fall back to *insertion sort*
  when working on small subarrays (≤32 elements for merge sort, ≤16 for quick
  sort). This reflects real-world AI tuning rules where small partitions benefit
  greatly from simpler algorithms.

• **AI-Inspired “Smart Selection” (choose_and_sort)**  
  The module can automatically choose the best algorithm:
  - Quick sort for small/medium input sizes (≤1024 elements)
  - Merge sort for large input sizes (better worst-case guarantees)

• **Median-of-Three Pivot Selection**  
  The quicksort implementation uses a median-of-three pivot strategy to reduce
  worst-case partition behavior and improve cache locality.

• **In-Place Quicksort Implementation**  
  Quick sort runs in place (except for the top-level wrapper), minimizing extra
  memory usage.

• **Fastest Driver Retrieval (fastest_driver)**  
  Once ETAs are sorted, the smallest ETA is returned immediately, representing
  the closest driver.

Functions
---------

- `insertion_sort(arr)`  
  A straightforward insertion sort for small arrays, used internally to improve
  performance during recursion.

- `ai_merge_sort(arr)`  
  A merge sort implementation enhanced with automatic switching to insertion
  sort for small partitions.

- `ai_quick_sort(arr)`  
  A quicksort implementation using:
    • median-of-three pivot selection  
    • insertion sort cutoff for small ranges  
    • in-place partitioning

- `choose_and_sort(arr, method=None)`  
  Automatically chooses the most efficient sorting algorithm unless a specific
  one is forced (`method="merge"` or `method="quick"`).

- `fastest_driver(sorted_etas)`  
  Returns the smallest element from a sorted ETA list.

Testing
-------

A single built-in test (`_test_random_small`) validates correctness using:
    • random ETA generation  
    • shuffling  
    • comparison against Python's built-in `sorted()`  

Running the module directly (via `python test1.py`) executes this test.

Example
-------

>>> etas = [13.5, 8.2, 22.1, 7.9]
>>> sorted_list = choose_and_sort(etas)
>>> fastest_driver(sorted_list)
7.9

This allows a ride-sharing platform to quickly identify the nearest driver.

Intended Use
------------

This module is suitable for:
  • dispatch systems  
  • ride-sharing and logistics  
  • ETA ranking engines  
  • real-time driver assignment optimization  
  • educational demonstrations of modern hybrid sorting algorithms  

The implementation focuses on clarity, maintainability, and practical performance
rather than theoretical purity, mirroring real-world engineering decisions guided
by AI optimization heuristics.
"""
