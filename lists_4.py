list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]


def dict_creator(a, b):
    result = [(a[i], b[i]) for i in range(len(a))]
    print(result)

dict_creator(list1, list2)
