# Optimized Python program for implementation of Bubble Sort
def bubble_sort(arr):
    """ Time Complexity: O(n²) worst/average, O(n) best case
    Space Complexity: O(1)
    Stable: YES
    In-place: YES
    
    Think: Bubbles rising to surface, heavy elements sink down""" 
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to check if any swap happened (optimization for best case)
        swapped = False
        # Last i elements are already in place
        for j in range(0,n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                # Swap if they're in wrong order
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if(swapped == False):
            break    

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted Array: ")
    for i in range(len(arr)):
        print("%d" % arr[i], end = " ")