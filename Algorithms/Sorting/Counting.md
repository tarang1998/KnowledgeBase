# Counting Sort

## Explanation

- Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array.
- The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.

### Working of Counting Sort

- Find out the maximum element (let it be max) from the given array.
  ![Given Array](https://cdn.programiz.com/cdn/farfuture/_iojSNQFxCvNdbdPPmMVCJZxGFTS0TOZRIt1E4Wte0Y/mtime:1582112622/sites/tutorial2program/files/Counting-sort-0_0.png)
- Initialize an array of length max+1 with all elements 0. This array is used for storing the count of the elements in the array.
  ![Count array](https://cdn.programiz.com/cdn/farfuture/bRDNfPQG8lie6m7EFXVqPj8w6RzkRhM34XNaAoG2dCs/mtime:1582112622/sites/tutorial2program/files/Counting-sort-1.png)
- Store the count of each element at their respective index in count array
  For example: if the count of element 3 is 2 then, 2 is stored in the 3rd position of count array. If element "5" is not present in the array, then 0 is stored in 5th position.
  ![Count of each stored element](https://cdn.programiz.com/cdn/farfuture/CIyC1Lkj5JFln_hjy8U1acmUZ4JST__v4bQBvPcnOkk/mtime:1582112622/sites/tutorial2program/files/Counting-sort-2.png)
- Store cumulative sum of the elements of the count array. It helps in placing the elements into the correct index of the sorted array.
  ![Cumulative Sort](https://cdn.programiz.com/cdn/farfuture/6A5S6vY-KsapHcyBjGgLNrp-58NRdyGDeVXspSzUbwM/mtime:1582112622/sites/tutorial2program/files/Counting-sort-3.png)
- Find the index of each element of the original array in the count array. This gives the cumulative count. Place the element at the index calculated as shown in figure below.
  ![Counting Sort](https://cdn.programiz.com/cdn/farfuture/tcfjQdeYwL_jETOCPZxNjIXbysRrb7MaG6PwO2MzHnM/mtime:1582112622/sites/tutorial2program/files/Counting-sort-4_1.png)
- After placing each element at its correct position, decrease its count by one

### Counting Sort Algorithm

```
countingSort(array, size)
  max <- find largest element in array
  initialize count array with all zeros
  for j <- 0 to size
    find the total count of each unique element and
    store the count at jth index in count array
  for i <- 1 to max
    find the cumulative sum and store it in count array itself
  for j <- size down to 1
    restore the elements to array
    decrease count of each element restored by 1
```

### Counting Sort Applications

Counting sort is used when:

- There are smaller integers with multiple counts.
- Linear complexity is the need.

## Articles

- [Counting Sort Algorithm](https://www.programiz.com/dsa/counting-sort)

## Complexity

### Time Complexity

There are mainly four main loops. (Finding the greatest value can be done outside the function.)

#### for-loop time of counting

- 1st O(max)
- 2nd O(size)
- 3rd O(max)
- 4th O(size)

Overall complexity = O(max)+O(size)+O(max)+O(size) = O(max+size)

- Worst Case Complexity: O(n+k)
- Best Case Complexity: O(n+k)
- Average Case Complexity: O(n+k)

In all the above cases, the complexity is the same because no matter how the elements are placed in the array, the algorithm goes through n+k times.

There is no comparison between any elements, so it is better than comparison based sorting techniques. But, it is bad if the integers are very large because the array of that size should be made.

### Space Complexity

The space complexity of Counting Sort is O(max). Larger the range of elements, larger is the space complexity.

### Stability

Yes

## Problems

### Fraudulent Activity Notification

- [Question](https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting)
- [Solutions](../../CompetitiveProgramming/Sorting/FraudulentActivityNotification/mergeSortCountingInversions.py)
