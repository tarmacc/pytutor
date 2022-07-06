def sorting_arr(lst):
    lst.sort()
    return sorted(lst, key=lst.count, reverse=True)