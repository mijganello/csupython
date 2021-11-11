dict1 = { 'trunk': 'хобот', 'wasted': 'потрачено' }
dict2 = { 'nail': 'гвоздь', 'trunk': 'ствол' }
dict3 = {}

def dict_creator(d1, d2, d3):

    for key,value in d1.items():
        if key in d2:
            for key1,value1 in d2.items():
                d3[key] = value1
        else:
            d3[key] = value

    for key,value in d2.items():
        if key not in d1:
            d3[key] = value
        

    return(d3)


result = dict_creator(dict1, dict2, dict3)
print(result)
