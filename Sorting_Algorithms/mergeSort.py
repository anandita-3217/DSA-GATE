def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    l = merge_sort(nums[:mid])
    r = merge_sort(nums[mid:])
    return merge(l,r)

def merge(left,right):
    i = j = 0
    result = []
    while i < len(left) and j <len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    merge_sort(arr)
    print("Sorted Array: ")
    print(*merge_sort(arr))