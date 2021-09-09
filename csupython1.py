words = ['lor', 'lorem', 'loremipsum', 'loremipsumdolor']
curlen = 0
maxlen = 0
l2 = 0
i = 0
for word in words:
    curlen = len(word)
    if curlen > maxlen:
        maxlen = curlen
        i += 1
    else :
        i += 1
print(maxlen)
