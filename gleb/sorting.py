def sorting(list):
    result = sorted(list, key=lambda x: (list.count(x), x), reverse=True)
    return result


print(sorting([2, 3, 5, 3, 7, 9, 5, 3, 7, 3, 5]))

