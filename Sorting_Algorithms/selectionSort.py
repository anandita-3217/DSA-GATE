"""
    🎯 SELECTION SORT - The Perfectionist
    
    Time Complexity: O(n²) in ALL cases
    Space Complexity: O(1)
    Stable: NO
    In-place: YES
    
    Think: Talent show - find the best, put them in final position
    """

"""
Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.

First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
We keep doing this until we get all elements moved to correct position.
"""
def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(arr)
    print("Sorted Array: ")
    for i in range(len(arr)):
        print("%d" % arr[i], end = " ")