# Merge Sort

## Explanation

- Merge Sort is one of the most popular sorting algorithms that is based on the principle of Divide and Conquer Algorithm.
- Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually. Finally, sub-problems are combined to form the final solution.
  ![Merge Sort](https://cdn.programiz.com/cdn/farfuture/PRTu8e23Uz212XPrrzN_uqXkVZVY_E0Ta8GZp61-zvw/mtime:1586425911/sites/tutorial2program/files/merge-sort-example_0.png)

### Divide and Conquer Strategy

- Using the Divide and Conquer technique, we divide a problem into subproblems. When the solution to each subproblem is ready, we 'combine' the results from the subproblems to solve the main problem.
- Suppose we had to sort an array A. A subproblem would be to sort a sub-section of this array starting at index p and ending at index r, denoted as A[p..r].

#### Divide

- If q is the half-way point between p and r, then we can split the subarray A[p..r] into two arrays A[p..q] and A[q+1, r].

#### Conquer

- In the conquer step, we try to sort both the subarrays A[p..q] and A[q+1, r]. If we haven't yet reached the base case, we again divide both these subarrays and try to sort them.

#### Combine

- When the conquer step reaches the base step and we get two sorted subarrays A[p..q] and A[q+1, r] for array A[p..r], we combine the results by creating a sorted array A[p..r] from two sorted subarrays A[p..q] and A[q+1, r].

## Complexity

- Time Complexity

  - Best Case Complexity: O(n\*log n)
  - Worst Case Complexity: O(n\*log n)
  - Average Case Complexity: O(n\*log n)

- Space Complexity

  - The space complexity of merge sort is O(n).

- Stability : Yes

## Problems

### Counting Inversions

- [Question](https://www.hackerrank.com/challenges/ctci-merge-sort/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting)
- [Solutions](../../CompetitiveProgramming%20/Sorting/MergeSort-CountingInversions/mergeSortCountingInversions.py)

## Articles

- [Merge Sort Algorithm](https://www.programiz.com/dsa/merge-sort)
