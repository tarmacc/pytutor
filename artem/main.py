def reverse_word(text):
    print(text[::-1])




 
def frequency_sort(items):
    a = sorted(items,key=items.count,reverse = True)
    return a




def low_to_up(line):
    data = iter(line)
    return ''.join([x.lower() + y.upper() for x,y in zip(data,data)])
    
