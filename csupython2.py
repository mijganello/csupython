words = ['lor','lorem','loremipsum','loremipsumdolor','aaaaaaa','oooooo']
less = []


for word in words:
    if len(word) < 5:
        less.append(word)


print(less)