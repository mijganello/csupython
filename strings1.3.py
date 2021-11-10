words = 'russia, iran, libia, usa, cucumber, yoptascript, dezoksiribonukleinovayakislota'
vowels = ['a', 'e', 'i', 'o', 'u']

def vowel_killer(list):
    new_string = ''
    for x in list:
        if x  not in vowels:
            new_string = new_string + x
        else:
            new_string += '*'

            
    print(new_string)


vowel_killer(words)
