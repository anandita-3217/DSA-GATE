def quick_sort(nums,low = 0,high=None):
    if high is None:
        high = len(nums) - 1
    if low< high:
        pivot = partition(nums,low,high)
        quick_sort(nums,low,pivot-1)
        quick_sort(nums,pivot+1,high)

def partition(nums,low,high):
    pivot = nums[high]
    i = low -1
    for j in range(low,high):
        if nums[j] <= pivot:
            i += 1
            nums[i],nums[j] = nums[j],nums[i]
    nums[i+1],nums[high] = nums[high],nums[i+1]
    return i + 1

def quick_sort_oneliner(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # pick middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_oneliner(left) + middle + quick_sort_oneliner(right)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick_sort_oneliner(arr)
    print("\nSorted Array quick sort oneliner: ")
    for i in sorted_arr:
        print("%d" % i, end = " ")

    arr1 = [64, 34, 25, 12, 22, 11, 90]
    quick_sort(arr1)
    print("\nSorted Array: ")
    for i in range(len(arr1)):
        print("%d" % arr1[i], end = " ")