def count(child_dict, i, depth=0):
    # Print entry into function with indentation to show recursion depth
    indent = "  " * depth
    print(f"{indent}Entering count(i={i}, depth={depth})")
    
    if i not in child_dict.keys():
        print(f"{indent}Node {i} has no children, returning 1")
        return 1
    
    ans = 1
    print(f"{indent}Node {i} has children: {child_dict[i]}")
    print(f"{indent}Starting with ans = {ans}")
    
    for j in child_dict[i]:
        print(f"{indent}Processing child {j}")
        child_count = count(child_dict, j, depth + 1)
        print(f"{indent}Child {j} contributed {child_count} nodes")
        ans += child_count
        print(f"{indent}Running total: ans = {ans}")
    
    print(f"{indent}Node {i} total count: {ans}")
    print(f"{indent}Exiting count(i={i})")
    return ans

if __name__ == "__main__":
    child_dict = dict()
    child_dict[0] = [1, 2]
    child_dict[1] = [3, 4, 5]
    child_dict[2] = [6, 7, 8]
    
    print("Tree structure:")
    for parent, children in child_dict.items():
        print(f"  {parent} -> {children}")
    print()
    
    print("Starting traversal:")
    result = count(child_dict, 0)
    print(f"\nFinal result: {result}")
    print("Solution")