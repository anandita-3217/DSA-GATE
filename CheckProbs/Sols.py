def count(child_dict,i):
    if i not in child_dict.keys():
        return 1
    ans = 1
    for j in child_dict[i]:

        ans += count(child_dict,j)
    return ans

if __name__ == "__main__":
    child_dict = dict()
    child_dict[0] = [1,2]
    child_dict[1] = [3,4,5]
    child_dict[2] = [6,7,8]
    count(child_dict,0)
    print("Solution")