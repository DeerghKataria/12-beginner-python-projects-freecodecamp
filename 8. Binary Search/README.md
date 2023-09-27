# Binary Search Algorithm

This Python script demonstrates the Binary Search algorithm. Binary Search is an efficient search algorithm used to find a target element in a sorted list. It repeatedly divides the search interval in half until the target element is found or the search interval becomes empty.

## Table of Contents

- [Introduction](#introduction)
- [Usage](#usage)
- [Performance Comparison](#performance-comparison)
- [License](#license)

## Introduction

This project consists of two main functions:

1. `naive_search(l, target)`: This function performs a naive linear search for the `target` element in a list `l`. It iterates through the list and returns the index of the target element if found, or -1 if not found.

2. `binary_search(l, target, low=None, high=None)`: This function implements the Binary Search algorithm. It searches for the `target` element in a sorted list `l`. It returns the index of the target element if found, or -1 if not found. It uses divide and conquer to efficiently locate the element.

## Usage

To use the binary search functions:

```python
# Import the functions
from binary_search import naive_search, binary_search

# Example list and target element
l = [1, 3, 5, 10, 22]
target = 10

# Perform a naive linear search
result_naive = naive_search(l, target)
print(f"Naive Search Result: {result_naive}")

# Perform a binary search (requires a sorted list)
result_binary = binary_search(l, target)
print(f"Binary Search Result: {result_binary}")
