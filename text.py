file = open('text.txt')
text1 = file.read()
file = open('text.txt')
text = file.readlines()

def counter(txt,txt1):
    line_count = 0
    word_count = 0
    punct_counter = 0
    puncts = ['.', ',', '?', '!', ';', ':', '-', '’','[', ']', '‒', '–', '—', '―', '...','“', '”', '‘', '’', '«', '»', '‹', '›']
    
    for x in txt:
        line_count+=1
    
    word_count = len(txt1.split())

    for x in txt1:
        if x in puncts:
            punct_counter+=1

    
    return(line_count, word_count, punct_counter)
    

result = counter(text,text1)
print(result)
