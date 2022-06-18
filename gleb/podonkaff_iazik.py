a = str(input()).lower()
for i in range(len(a)):
    if i % 2 !=0:
        print(a[i].upper(), end ='')
    else:
        print(a[i], end ='')
