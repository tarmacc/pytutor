# Задача 1
def reverse_word(text):
    print(text[::-1])

reverse_word('artem')


# Задача 2 Полунагугленная
# Возникла сложность с цифрами'5' и '7' тк их по 2. С неравным кол-ом проблем не возникает
# Задача сложная, я бы ее разобрал   
def frequency_sort(items):
    a = sorted(items,key=items.count,reverse = True)
    return a

print(frequency_sort([2,3,5,3,7,9,5,3,7,3,5]))


# Задача 3 полность нагулил, ниже описал свой вариант
# Задач очень сложная, тоже разобрал бы как ее решить легко
def low_to_up(line):
    data = iter(line)
    return ''.join([x.lower() + y.upper() for x,y in zip(data,data)])
    
print(low_to_up(input()))

# Я бы решил конкатенацией индекса, если брать за условие конкретную строку 'Йазык Падонкаф', а не любые вводимые данные
# text = input().upper()
# print(text[0].lower+text[1] .... и тд)

