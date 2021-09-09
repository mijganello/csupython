words = ['lor','lorem','loremipsum','loremipsumdolor','aaaaaaa','oooooo']
vowel = ['a','e','i','o','u','y']
vowel_w = []
cons_w = []

for word in words:
    if word[0] in vowel:
        vowel_w.append(word)
    else:
        cons_w.append(word)


print('Список гласных : ', vowel_w)
print('Список согласных: ', cons_w)
