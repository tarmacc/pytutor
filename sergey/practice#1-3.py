string = 'жаргон падонкаф'
string1 = ''
for s in string:
    if s.isupper():
        string1 += s.lower()
    else:
        string1 += s.upper()
print(string1)