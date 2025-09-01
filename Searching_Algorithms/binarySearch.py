# Will work only for sorted arrays
def binary_search(nums,target):
    """
    🔍 BINARY SEARCH - The Divide & Conquer Champion
    
    Time Complexity: O(log n) - cuts array in half each time
    Space Complexity: O(1) - only uses few variables
    
    PRECONDITION: Array MUST be sorted!
"""
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = l + (r-l) //2
        if nums[mid] == target:
            return [True, mid]
        elif nums[mid] < target:
            l = mid + 1
        else:
            r  = mid - 1
    return [False,-1]

if __name__ == "__main__":
    nums = [10, 20, 30, 50, 60, 70]
    print(binary_search(nums,30))