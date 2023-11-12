def recursive_search(lst, target):
    if lst == []:
        return -1
    elif lst[0] == target:
        return 0
    res = recursive_search(lst[1:], target)
    if res < 0:
        return res
    return res + 1
lst = [1, 2, 3, 4, 5, 6, 7]
target = 4 
print(recursive_search(lst,target)) 