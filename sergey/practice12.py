#list = [2,3,5,3,7,9,5,3,7]#обозначаем
def second_sort(list):
    list = [2,3,5,3,7,9,5,3,7]#обозначаем
    list.sort()#сортируем
    return sorted(list, key=list.count, reverse=True)
second_sort()