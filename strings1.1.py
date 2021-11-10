words = 'russia, iran, libia, usa, cucumber, yoptascript, dezoksiribonukleinovayakislota'


def word_count(list):
    n = 0
    for x in list:
        if x == ' ':
            n+=1
    print(n+1)


    

word_count(words)
