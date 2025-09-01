def insertion_sort(arr):
    """Insertion sort is a simple sorting algorithm that works by iteratively 
inserting each element of an unsorted list into its correct position 
in a sorted portion of the list. 
It is like sorting playing cards in your hands. 
You split the cards into two groups: the sorted cards and the unsorted cards. 
Then, you pick a card from the unsorted group and put it in the right place in the sorted group.

- We start with the second element of the array as the first element is assumed to be sorted.
- Compare the second element with the first element if the second element is smaller then swap them.
- Move to the third element, compare it with the first two elements, and put it in its correct position
- Repeat until the entire array is sorted.

    🃏 INSERTION SORT - The Card Player
    
    Time Complexity: O(n²) worst/average, O(n) best case
    Space Complexity: O(1)
    Stable: YES
    In-place: YES
    
    Think: Sorting cards in your hand - insert each new card in right place
    """

    n = len(arr)
    for i in range(1,n):
        key = arr[i] # Current element to be inserted
        j = i - 1 # Start of sorted portion
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]  # Shift right
            j -= 1
        arr[j+1] = key # Insert key at its correct position
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    print("Sorted Array: ")
    for i in range(len(arr)):
        print("%d" % arr[i], end = " ")