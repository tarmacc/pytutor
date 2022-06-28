def letter(word):
    empty = []
    for i, j in enumerate(word):  # possible use of range func
        if i % 2 != 0:
            empty.append(word[i].upper())
        else:
            empty.append(word[i])
    final = ''.join(empty)
    return final

def iazik(text):
    new_text, l = text.lower().split(), []
    for j in new_text:
        l.append(letter(j))
    result = ' '.join(l)
    return result

#print(iazik('aasadasd!! aa sasW'))