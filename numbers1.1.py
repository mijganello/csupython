def mybin(n):
    d1 = 10
    d2 = 2
    number = ''
    result = ''
    if n > 0:
        while d2 <= n:
            number = number + str(n%d2)
            n = n//d2
            result = str(n) + number[::-1]
    else:
        n = abs(n)
        while d2 <= n:
            number = number + str(n%d2)
            n = n//d2
            result = '-' + str(n) + number[::-1]

        
    
    print(result, type(number))


mybin(100)
