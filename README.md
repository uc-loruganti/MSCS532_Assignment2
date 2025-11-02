
# Merge Sort vs. Quick Sort Analysis

This project provides Python implementations of Merge Sort and Quick Sort algorithms and a script to analyze their performance.

## How to Run

### Individual Sorting Algorithms

You can run each sorting algorithm individually by passing a list of integers as command-line arguments.

**Merge Sort:**
```bash
python merge_sort.py --elements 10 5 2 8 7 1 9 4 6 3
```

**Quick Sort:**
```bash
python quick_sort.py --elements 10 5 2 8 7 1 9 4 6 3
```

### Performance Analysis

To compare the performance of the two algorithms, you can run the `performance_analysis.py` script. This will generate datasets of different sizes and types (random, sorted, reverse-sorted) and run the sorting algorithms on them, measuring execution time and memory usage.

```bash
python performance_analysis.py
```

The script will print a markdown table with the performance results.
