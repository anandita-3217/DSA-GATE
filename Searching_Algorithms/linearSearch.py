"""
    🔍 LINEAR SEARCH - The Brute Force Hero
    
    Time Complexity: O(n) - worst case checks every element
    Space Complexity: O(1) - no extra space needed
    
    Returns: [found (bool), index (int)]
"""
def linear_search(nums,target):
    for i in range(len(nums)):  # Use index-based loop!
        if nums[i] == target:
            return [True, i]        # Return the ACTUAL index we found
    return [False, -1]
# 🔄 Alternative Implementations (Good to know for GATE)

def linear_search_pythonic(nums, target):
    """
    More Pythonic version using enumerate
    """
    for index, value in enumerate(nums):
        if value == target:
            return [True, index]
    return [False, -1]


def linear_search_with_details(nums, target):
    """
    Detailed version that shows comparisons (useful for GATE analysis)
    """
    comparisons = 0
    
    for i in range(len(nums)):
        comparisons += 1
        if nums[i] == target:
            return [True, i, comparisons]
    
    return [False, -1, comparisons]


def linear_search_all_occurrences(nums, target):
    """
    Find ALL occurrences - sometimes asked in GATE
    """
    indices = []
    
    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)
    
    if indices:
        return [True, indices]
    return [False, []]


if __name__ == "__main__":
    nums = [10, 20, 30, 50, 40, 60, 40, 70]
    print(linear_search(nums,70))