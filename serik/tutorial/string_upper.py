string ='undergroud'
num = 0
new_word = []
for i in string:
    if num % 2 == 0:
        num += 1
        new_word.append(i.upper())
    else:
        num += 1
        new_word.append(i.lower())
print(new_word)
