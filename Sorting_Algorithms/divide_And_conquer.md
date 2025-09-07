# Merge Sort & Quick Sort - GATE 2026 Cheat Sheet

## 🤝 MERGE SORT - "The Reliable Friend"

### Key Points
- **Time:** Always O(n log n) - no surprises!
- **Space:** O(n) - needs extra arrays
- **Stable:** Yes - maintains order of equal elements
- **Strategy:** Divide → Sort → Merge

### Python Code
```python
def merge_sort(arr):
    # BASE CASE: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
    
    # DIVIDE: split array in half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # recursively sort left half
    right = merge_sort(arr[mid:])   # recursively sort right half
    
    # CONQUER: merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:     # <= for stability
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements (if any)
    result.extend(left[i:])   # add leftover from left
    result.extend(right[j:])  # add leftover from right
    
    return result
```

### Memory Trick
**"Split it, Sort it, Stitch it back together"**

---

## 🎯 QUICK SORT - "The Fast but Dramatic One"

### Key Points
- **Time:** Average O(n log n), Worst O(n²)
- **Space:** O(log n) - in-place sorting
- **Stable:** No - can change order of equal elements
- **Strategy:** Pick pivot → Partition → Recurse

### Python Code (Lomuto Partition)
```python
def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    # BASE CASE: if low >= high, we're done
    if low < high:
        # PARTITION: find pivot position
        pivot_index = partition(arr, low, high)
        
        # RECURSE: sort left and right of pivot
        quick_sort(arr, low, pivot_index - 1)      # left side
        quick_sort(arr, pivot_index + 1, high)     # right side

def partition(arr, low, high):
    # Choose last element as pivot
    pivot = arr[high]
    i = low - 1  # index of smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # return pivot position
```

### Alternative: One-liner Quick Sort (easier to remember!)
```python
def quick_sort_oneliner(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # pick middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort_oneliner(left) + middle + quick_sort_oneliner(right)
```

### Memory Trick
**"Pick, Partition, and Pounce on both sides"**

---

## 🆚 Quick Comparison

| Feature | Merge Sort | Quick Sort |
|---------|------------|------------|
| **Best Case** | O(n log n) | O(n log n) |
| **Average Case** | O(n log n) | O(n log n) |
| **Worst Case** | O(n log n) | O(n²) |
| **Space** | O(n) | O(log n) |
| **Stable** | ✅ Yes | ❌ No |
| **In-place** | ❌ No | ✅ Yes |

## 🧠 GATE Exam Tips

### When to use which?
- **Need guaranteed performance?** → Merge Sort
- **Limited memory?** → Quick Sort
- **Need stability?** → Merge Sort
- **Already implemented in libraries?** → Quick Sort (usually)

### Common GATE Questions:
1. **Recurrence relations:** 
   - Merge: T(n) = 2T(n/2) + O(n)
   - Quick: T(n) = T(k) + T(n-k-1) + O(n)

2. **Number of comparisons:**
   - Merge: Always ≈ n log n
   - Quick: Best ≈ n log n, Worst ≈ n²/2

3. **Stack depth:**
   - Merge: O(log n)
   - Quick: Best O(log n), Worst O(n)

### Quick Memory Aids
- **Merge:** "Reliable but needs backup storage"
- **Quick:** "Usually fast, but pick pivots wisely!"
- **Stability:** "Merge keeps things steady, Quick might shuffle equals"