file = open('text.txt')
text = file.read()


def counter(txt):
    line_count = 0
    word_count = 0
    punct_counter = 0
    puncts = ['.', ',', '?', '!', ';', ':', '-', '’','[', ']', '‒', '–', '—', '―', '...','“', '”', '‘', '’', '«', '»', '‹', '›']
    
    for x in txt:
        line_count+=1
    
    word_count = len(txt.split())

    for x in txt:
        if x in puncts:
            punct_counter+=1

    
    return(line_count, word_count, punct_counter)
    





result = counter(text)
print(result)
